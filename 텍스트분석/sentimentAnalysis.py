import pandas as pd
from pandas import Series
import numpy as np
import re
from sklearn.cross_validation import train_test_split


import json 
import os 
from pprint import pprint 

from konlpy.tag import Okt
import nltk


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


print(sentiment_class[4050:4100])
print(data[4050:4100][['NAVER_PRE_EVAL', 'NAVER_SENTIMENT']]) 
 
 
# 0: 부정 / 1 : 긍정 / 2: 중립 / 3: nan
for idx in range( len(data) ):
    cond1 = data['NAVER_PRE_EVAL'][idx] > 4
    cond2 = data['NAVER_PRE_EVAL'][idx] < 7
    
    if data['NAVER_PRE_EVAL'][idx] >= 7:
        sentiment.append(1)
    elif data['NAVER_PRE_EVAL'][idx] <= 4:
        sentiment.append(0)
#     elif (4 < data['NAVER_PRE_EVAL'][idx] < 7) :
#         sentiment.append(np.nan)
    else : 
        sentiment.append(np.NaN)

# print(sentiment[0:100])

data['NAVER_SENTIMENT'] = Series(sentiment)

# print( data['NAVER_SENTIMENT'][3980:4000] )
# print( sentiment[3980:4000] )
# print( sentiment[3993] )

 
data['NAVER_CMT'] = \
                data['NAVER_CMT'].apply(lambda x : re.sub('[^0-9a-zA-Zㄱ-힗 ]', '', str(x)))
   
# print(data.tail(100)) 
                       
train_data, test_data = train_test_split(data, test_size = 0.2)
  
print(data.columns)
   
okt = Okt()
  
  
# tagging = okt.pos()
      
def tokenize(doc):
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]
#   
# if os.path.isfile('train_docs.json'):
#     with open('train_docs.json') as f:
#         train_docs = json.load(f)
#     with open('test_docs.json') as f:
#         test_docs = json.load(f)
# else:
#     train_docs = [(tokenize(row[2]), row[4]) for row in train_data]
#     test_docs = [(tokenize(row[2]), row[4]) for row in test_data]
#     # JSON 파일로 저장
#     with open('train_docs.json', 'w', encoding="utf-8") as make_file:
#         json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
#     with open('test_docs.json', 'w', encoding="utf-8") as make_file:
#         json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")
# 
# pprint(train_docs[0:100])


print( [ tokenize(row[0]) for row in train_data[0:10] ])

 
 
# train_docs = [() for row in train_data]

# print(okt.pos(data['NAVER_CMT'][0], norm=True, stem=True)[0:10])











# if os.path.isfile('train_docs.json'):
#     with open('train_docs.json') as f:
#         train_docs = json.load(f)
#     with open('test_docs.json') as f:
#         test_docs = json.load(f)
# else:
#     train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
#     test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
#     with open('train_docs.json', 'w', encoding="utf-8") as make_file:
#         json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
#     with open('test_docs.json', 'w', encoding="utf-8") as make_file:
#         json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")
# 
# 
# pprint(train_docs[0][0:10])

# pprint(train_docs[0])



#  
# okt = Okt()
#  
# train_docs = okt.pos(data['NAVER_CMT'][0])[0:10]
# print(train_docs)
#  
# tokens = [t for d in train_docs for t in d[0]]
# print(len(tokens))











# text = data['NAVER_CMT'][0]
# 
# okt = Okt()
# 
# def tokenize(text):
#     return [okt.pos(text, norm=True, stem=True)]














# text = data['NAVER_CMT'][0]
#  
# okt = Okt()
# tagging = okt.pos(text)
#  
# print(tagging[0:10])
# print('-'*50)








 
# stop_words = ['영화']
#   
#   
# def get_tags(text, ntags):
#     nouns = nltk.pos_tag(text)
#     wcData = nouns.vocab().most_common(ntags)
#     wcDict = dict(wcData)
#     return wcDict
#     
# wcInput = get_tags(text, 100)
# print(sorted(wcInput.items(), key=lambda x:x[1], reverse=True))