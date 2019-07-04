import pandas as pd 
import re
from konlpy.tag import Okt
from konlpy.tag._komoran import Komoran
from sklearn.cross_validation import train_test_split




import numpy as np
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
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.linear_model import LogisticRegression

import tensorflow as tf 
import random



data = pd.read_csv('D:/myworkspace/github/movie.csv', encoding='utf-8')
data = data[['TITLE', 'OPEN_DT', 'PLOT', 'AUDI_ACC']]
data = data.dropna()

data['PLOT'] = data['PLOT'].apply(lambda x : re.sub('[^0-9a-zA-Zㄱ-힗 ]', ' ', str(x)))

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


data['TOKEN_PLOT'] = data['PLOT'].apply(tokenizer_okt_morphs)

data = data[0:2] #########나중에 지우기
 
# documents = [TaggedDocument(doc, [i]) for morphList in data['TOKEN_PLOT'] for i, doc in enumerate(morphList) ]
#   
# print(documents[0])
# 
# for text in data['PLOT']:
#     print(text)
#     break

cnt = 1
for morphList in data['TOKEN_PLOT']:
    for i, doc in enumerate(morphList):
        print(i, doc)
        cnt += 1 
        if cnt <=10:
            break





# okt = Okt()
# def tokenizer_okt_morphs(doc):
#     return okt.morphs(doc)
#    
# def tokenizer_okt_nouns(doc):
#     return okt.nouns(doc)
#    
# def tokenizer_okt_pos(doc):
#     return okt.pos(doc, norm=True, stem=True)
# 
# komoran = Komoran()
# def tokenizer_nouns(doc):
#     return komoran.nouns(doc)
#     
# def tokenizer_morphs(doc):
#     return komoran.morphs(doc)


# # stop_words = ['은', '는', '이', '가', '을', '를', '에', '의', '과', '와', '둘', '등']
# data['TOKEN_PLOT'] = data['PLOT'].apply(tokenizer_okt_morphs)
# # train_data['TOKEN_CMT'] = [each_word for each_word in train_data['TOKEN_CMT'] if each_word not in stop_words ]
# 
# data = data[:10]
# 
# train_data, test_data = train_test_split(data, test_size = 0.2)
# 
# 
# 
# taggedDocument = namedtuple('taggedDacument', ['words', 'tags'])
#    
# # d: 댓글내용 / c: sentiment class
# tagged_train_docs = [ taggedDocument(d, c) for d, c in train_data[['TOKEN_PLOT', 'AUDI_ACC']].values ]
# tagged_test_docs = [taggedDocument(d, c) for d, c in test_data[['TOKEN_PLOT', 'AUDI_ACC']].values ]
# 
# 
# # print(train_data['PLOT'][0][0])
# # print(tagged_train_docs[0][0])
# 
# 
# cores = multiprocessing.cpu_count()
# # print(cores)
#       
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#       
#       
#       
#       
# doc_vectorizer = Doc2Vec(
#     dm=0,            
#     dbow_words=1,    
#     window=8,        
#     vector_size=300,        
#     alpha=0.025,     
#     seed=1234,
#     min_count=20,    
#     min_alpha=0.025, 
#     workers=cores,   
#     hs = 1,          
#     negative = 10,   
# )
#      
# doc_vectorizer.build_vocab(tagged_train_docs)
# # print(str(doc_vectorizer))
# # print(doc_vectorizer.corpus_count)
# # print(doc_vectorizer.iter)
#    
# start = time()
# for epoch in range(10):
#     doc_vectorizer.train(tagged_train_docs, total_examples=doc_vectorizer.corpus_count, epochs=doc_vectorizer.iter)
#     doc_vectorizer.alpha -= .002 
#     doc_vectorizer.min_alpha = doc_vectorizer.alpha 
# end = time()
# print('During Time : {}'.format(end-start))
#         
# model_name = 'sent_doc2vec.model'
# doc_vectorizer.save(model_name)
#    
# sentAnalyzer = Doc2Vec.load('sent_doc2vec.model')
# # print(sentAnalyzer.wv.most_similar('액션'))
#    
# ########word_embedding : doc2vec

print('finished')