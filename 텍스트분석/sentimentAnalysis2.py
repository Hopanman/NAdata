import pandas as pd
import numpy as np
import re
from sklearn.cross_validation import train_test_split
from konlpy.tag import Okt
from konlpy.tag._komoran import Komoran
import nltk
import seaborn as sns

import json 
import os 
from pprint import pprint 







data = pd.read_csv('D:\myworkspace\github\movie.csv', encoding='utf-8')
data = data[['TITLE', 'OPEN_DT', 'NAVER_CMT', 'NAVER_PRE_EVAL']]

# print( data.info() )

sentiment_class = [
    "POS" if data.iloc[i]['NAVER_PRE_EVAL'] >= 8
    else
    "NEU" if data.iloc[i]['NAVER_PRE_EVAL'] >= 4
    else
    "NEG" if 0 < data.iloc[i]['NAVER_PRE_EVAL'] < 4
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

########
train_data = train_data[0:2]

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

# test_data['TOKEN_CMT'] = test_data['NAVER_CMT'].apply(tokenizer_okt_morphs)

# print( train_data[['TOKEN_CMT', 'NAVER_CMT']].head() )

tokens = [ t for d in train_data['TOKEN_CMT'] for t in d ]
# print(tokens)

# print(len(tokens))


text = nltk.Text(tokens)
# print(len(text.tokens))
# print(len(set(text.tokens)))
print(text.vocab().most_common(10))


text.plot(20)

print('finished')