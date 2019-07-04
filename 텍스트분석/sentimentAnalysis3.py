import pandas as pd
import numpy as np
import re
from sklearn.cross_validation import train_test_split
from konlpy.tag import Okt
from konlpy.tag._komoran import Komoran
import nltk
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from time import time
from collections import namedtuple
import multiprocessing
import logging
from gensim.models.doc2vec import Doc2Vec
from sklearn.linear_model import LogisticRegression

import tensorflow as tf 
import random



# np.random.seed(100)

# FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`. 
# 위 오류 해결하려면 cmd에서 업그레이드
# pip install --upgrade h5py
# pip install --upgrade numpy 
 
 
 
data = pd.read_csv('D:/myworkspace/github/movie.csv', encoding='utf-8')
data = data[['TITLE', 'OPEN_DT', 'NAVER_CMT', 'NAVER_PRE_EVAL']]
data = data.dropna()
###########na 값 처리하기

######## 데이터 양 많아서 테스트용으로 함(나중에 지우기)
data = data[3950:4000]
 
# print( data.info() )
 
sentiment_class = [
    "POS" if data.iloc[i]['NAVER_PRE_EVAL'] >= 8
    else
    "NEU" if data.iloc[i]['NAVER_PRE_EVAL'] >= 4
    else
    "NEG"
    for i in range(len(data)) 
    ]

data['NAVER_SENTIMENT'] = sentiment_class
# print(sentiment_class[4050:4100])
# print(data[4050:4100][['NAVER_PRE_EVAL', 'NAVER_SENTIMENT']]) 
  
data['NAVER_CMT'] = \
                data['NAVER_CMT'].apply(lambda x : re.sub('[^0-9a-zA-Zㄱ-힗 ]', '', str(x)))
# print(data.tail(100)) 
 
train_data, test_data = train_test_split(data, test_size = 0.2)
 
okt = Okt()
def tokenizer_okt_morphs(doc):
    return okt.morphs(doc)
   
def tokenizer_okt_nouns(doc):
    return okt.nouns(doc)
   
def tokenizer_okt_pos(doc):
    return okt.pos(doc, norm=True, stem=True)
   
komoran = Komoran()
def tokenizer_nouns(doc):
    return komoran.nouns(doc)
    
def tokenizer_morphs(doc):
    return komoran.morphs(doc)

# SettingWithCopyWarning 해결하기 위한 코드
pd.options.mode.chained_assignment = None 

# stop_words = ['은', '는', '이', '가', '을', '를', '에', '의', '과', '와', '둘', '등']

train_data['TOKEN_CMT'] = train_data['NAVER_CMT'].apply(tokenizer_okt_morphs)
# train_data['TOKEN_CMT'] = [each_word for each_word in train_data['TOKEN_CMT'] if each_word not in stop_words ]

test_data['TOKEN_CMT'] = test_data['NAVER_CMT'].apply(tokenizer_okt_morphs)
# test_data['TOKEN_CMT'] = [each_word for each_word in test_data['TOKEN_CMT'] if each_word not in stop_words ]

# print(train_data['TOKEN_CMT'][0:10])
 
    
# print( train_data[['TOKEN_CMT', 'NAVER_CMT']].head() )
     
tokens = [ t for d in train_data['TOKEN_CMT'] for t in d ]
# print(tokens)
# print(len(tokens))
     
text = nltk.Text(tokens)
# print(len(text.tokens))
# print(len(set(text.tokens)))
print(text.vocab().most_common(10))
    
# sns.set_style('darkgrid')
# sns.set_palette('hls')
# text.plot(20)
    
# text.concordance('영화')
    
x_train = train_data.loc[:, 'NAVER_CMT'].values 
y_train = train_data.loc[:, 'NAVER_SENTIMENT'].values
  
  
# ######### tf-idf 모델 : Naive Bayes
# 
# tfidf = TfidfVectorizer(tokenizer=tokenizer_morphs)
# # tfidf = TfidfVectorizer(tokenizer=tokenizer_nouns)
#   
# multi_nbc = Pipeline([('vect', tfidf), ('nbc', MultinomialNB())])
#   
# start = time()
# multi_nbc.fit(x_train, y_train)
# end = time()
# # print('Time: {:f}s'.format(end-start))
#   
# y_pred = multi_nbc.predict(test_data['NAVER_CMT'])
# # print("테스트 정확도: {:.3f}".format(accuracy_score(test_data['NAVER_SENTIMENT'], y_pred)))
# 
# 
# ######### tf-idf 모델
  
  
  
  
  
########word_embedding : doc2vec
    
taggedDocument = namedtuple('taggedDacument', ['words', 'tags'])
   
# d: 댓글내용 / c: sentiment class
tagged_train_docs = [ taggedDocument(d, c) for d, c in train_data[['TOKEN_CMT', 'NAVER_SENTIMENT']].values ]
tagged_test_docs = [taggedDocument(d, c) for d, c in test_data[['TOKEN_CMT', 'NAVER_SENTIMENT']].values ]
     
# print(len(data))
# print(len(tagged_train_docs), len(tagged_test_docs))
   
#cpu_core의 수  
cores = multiprocessing.cpu_count()
# print(cores)
     
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
     
doc_vectorizer = Doc2Vec(
    dm=0,            
    dbow_words=1,    
    window=8,        
    vector_size=300,        
    alpha=0.025,     
    seed=1234,
    min_count=20,    
    min_alpha=0.025, 
    workers=cores,   
    hs = 1,          
    negative = 10,   
)
     
doc_vectorizer.build_vocab(tagged_train_docs)
# print(str(doc_vectorizer))
# print(doc_vectorizer.corpus_count)
# print(doc_vectorizer.iter)
   
start = time()
for epoch in range(10):
    doc_vectorizer.train(tagged_train_docs, total_examples=doc_vectorizer.corpus_count, epochs=doc_vectorizer.iter)
    doc_vectorizer.alpha -= .002 
    doc_vectorizer.min_alpha = doc_vectorizer.alpha 
end = time()
print('During Time : {}'.format(end-start))
        
model_name = 'sent_doc2vec.model'
doc_vectorizer.save(model_name)
   
sentAnalyzer = Doc2Vec.load('sent_doc2vec.model')
# print(sentAnalyzer.wv.most_similar('액션'))
   
########word_embedding : doc2vec
  
  
  
  
  
########모델 학습 / 평가 : doc2vec
###데이터 셋 나누기
x_train = [doc_vectorizer.infer_vector(doc.words) for doc in tagged_train_docs]
y_train = [doc.tags for doc in tagged_train_docs]
  
x_test = [doc_vectorizer.infer_vector(doc.words) for doc in tagged_test_docs]
y_test = [doc.tags for doc in tagged_test_docs]
  
# print(len(x_train), len(y_train))
  
y_train_np = np.asarray([0 if c == 'NEG' else 1 if c == 'NEU' else 2 for c in y_train], dtype=int)
y_test_np = np.asarray([0 if c == 'NEG' else 1 if c == 'NEU' else 2 for c in y_test], dtype=int)
  
x_train_np = np.asarray(x_train)
x_test_np = np.asarray(x_test)
  
# print(len(x_train_np[0]), len(x_test_np[0]))
  
# print(x_train_np.shape)
# print(y_train_np)
  
y_train_np = np.eye(3)[y_train_np.reshape(-1)]
y_test_np = np.eye(3)[y_test_np.reshape(-1)]
  
  
######데이터 셋 나누기
  
  
# #############logistic Regression
# 
# clf = LogisticRegression(random_state=1234)
#  
# start = time()
# clf.fit(x_train, y_train)
# end = time()
# print('Time : {:f}s'.format(end-start))
#  
# y_pred = clf.predict(x_test)
# print('테스트 정확도: {:.3f}'.format(accuracy_score(y_pred, y_test)))
# 
# #############logistic Regression
  
  
  
  
############deep neural learning 
tf.reset_default_graph()
  
learning_rate = 0.001 
training_epochs = 15
batch_size = 100 
  
x = tf.placeholder(tf.float32, [None, 300])
y = tf.placeholder(tf.float32, [None, 3])
  
keep_prob = tf.placeholder(tf.float32)
  
xavier_init = tf.contrib.layers.xavier_initializer()
  
w1 = tf.get_variable('w1', shape=[300, 256], initializer=xavier_init)
b1 = tf.Variable(tf.random_normal([256]))
l1 = tf.nn.relu(tf.matmul(x, w1)+b1)
dropout1 = tf.nn.dropout(l1, keep_prob=keep_prob)
  
w2 = tf.get_variable('w2', shape=[256, 256], initializer=xavier_init)
b2 = tf.Variable(tf.random_normal([256]))
l2 = tf.nn.relu(tf.matmul(dropout1, w2)+b2)
dropout2 = tf.nn.dropout(l2, keep_prob=keep_prob)
  
w3 = tf.get_variable('w3', shape=[256, 256], initializer=xavier_init)
b3 = tf.Variable(tf.random_normal([256]))
l3 = tf.nn.relu(tf.matmul(dropout2, w3)+b3)
dropout3 = tf.nn.dropout(l3, keep_prob=keep_prob)
  
w4 = tf.get_variable('w4', shape=[256, 256], initializer=xavier_init)
b4 = tf.Variable(tf.random_normal([256]))
l4 = tf.nn.relu(tf.matmul(dropout3, w4)+b4)
dropout4 = tf.nn.dropout(l4, keep_prob=keep_prob)
  
w5 = tf.get_variable('w5', shape=[256, 3], initializer=xavier_init)
b5 = tf.Variable(tf.random_normal([3]))
hypothesis = tf.matmul(dropout4, w5)+b5
  
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
  
saver = tf.train.Saver()
save_file = './deepNeural_imsi.ckpt'
  
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
      
    for epoch in range(training_epochs):
        avg_cost = 0 
        total_batch = int( len(x_train_np) / batch_size)
          
        for i in range(0, len(x_train_np), batch_size):
            batch_xs = x_train_np[i:i+batch_size]
            batch_ys = y_train_np[i:i+batch_size]
      
            feed_dict = {x:batch_xs, y: batch_ys, keep_prob:0.7}
            c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
            avg_cost += c / total_batch
      
        print('Epoch:', '{:04d}'.format(epoch +1), 'cost =', '{:.9f}'.format(avg_cost))
          
        saver.save(sess, save_file)
        print('trained model saved')
print('Training Finished')
  
    
with tf.Session() as sess:
    saver.restore(sess, save_file)
    correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    test_accuracy = sess.run(accuracy, feed_dict={x: x_test_np ,y:y_test_np, keep_prob:1 }) 
    print('테스트 정확도: ', test_accuracy)
        
print('finished')