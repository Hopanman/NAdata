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
 
 
 
import json 
import os 
from pprint import pprint 

 
 
 
 
 
 
 
data = pd.read_csv('C:/Users/user/Documents/github/movie.csv', encoding='utf-8')
data = data[['TITLE', 'OPEN_DT', 'NAVER_CMT', 'NAVER_PRE_EVAL']]

###########na 값 처리하기


 
# print( data.info() )
 
sentiment_class = [
    "POS" if data.iloc[i]['NAVER_PRE_EVAL'] >= 7
    else
    "NEU" if data.iloc[i]['NAVER_PRE_EVAL'] >= 5
    else
    "NEG" if 0 < data.iloc[i]['NAVER_PRE_EVAL'] < 5
    else
    np.nan
    for i in range(len(data)) 
    ]
 
data['NAVER_SENTIMENT'] = sentiment_class
# print(sentiment_class[4050:4100])
# print(data[4050:4100][['NAVER_PRE_EVAL', 'NAVER_SENTIMENT']]) 
  
data['NAVER_CMT'] = \
                data['NAVER_CMT'].apply(lambda x : re.sub('[^0-9a-zA-Zㄱ-힗 ]', '', str(x)))
# print(data.tail(100)) 
 
train_data, test_data = train_test_split(data, test_size = 0.2)
 
######## 데이터 양 많아서 테스트용으로 함(나중에 지우기)
train_data = train_data[0:2]
test_data = test_data[0:2]
 
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
 
train_data['TOKEN_CMT'] = train_data['NAVER_CMT'].apply(tokenizer_okt_morphs)
 
test_data['TOKEN_CMT'] = test_data['NAVER_CMT'].apply(tokenizer_okt_morphs)
 
# print( train_data[['TOKEN_CMT', 'NAVER_CMT']].head() )
 
tokens = [ t for d in train_data['TOKEN_CMT'] for t in d ]
# print(tokens)
 
# print(len(tokens))
 
 
text = nltk.Text(tokens)
# print(len(text.tokens))
# print(len(set(text.tokens)))
# print(text.vocab().most_common(10))

# sns.set_style('darkgrid')
# sns.set_palette('hls')
# text.plot(20)

# text.concordance('영화')

x_train = train_data.loc[:, 'NAVER_CMT'].values 
y_train = train_data.loc[:, 'NAVER_SENTIMENT'].values

tfidf = TfidfVectorizer(tokenizer=tokenizer_morphs)

multi_nbc = Pipeline([('vect', tfidf), ('nbc', MultinomialNB())])

start = time()
multi_nbc.fit(x_train, y_train)
end = time()
# print('Time: {:f}s'.format(end-start))

#######NAVER_CMT, NAVER_SENTIMENT -> 맞는지 확인하기
x_test = test_data.loc[:, 'NAVER_CMT'].values 
y_test = test_data.loc[:, 'NAVER_SENTIMENT'].values

y_pred = multi_nbc.predict(test_data['NAVER_CMT'])
# print("테스트 정확도: {:.3f}".format(accuracy_score(test_data['NAVER_SENTIMENT'], y_pred)))

taggedDocument = namedtuple('taggedDaocument', 'words tags')

tagged_train_docs = [ taggedDocument(d, c) for d, c in train_data[['TOKEN_CMT', 'NAVER_SENTIMENT']].values ]
tagged_test_docs = [taggedDocument(d, c) for d, c in test_data[['TOKEN_CMT', 'NAVER_SENTIMENT']].values ]

# print(len(data))
# print(len(tagged_train_docs), len(tagged_test_docs))

cores = multiprocessing.cpu_count()
# print(cores)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

doc_vectorizer = Doc2Vec(
    dm=0,            
    dbow_words=1,    
    window=8,        
    size=300,        
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

model_name = 'doc2vec.model'
doc_vectorizer.save(model_name)

print('finished')