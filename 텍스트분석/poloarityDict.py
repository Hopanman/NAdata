import pandas as pd
import re
from konlpy.tag import Okt
from konlpy.tag._komoran import Komoran
import numpy as np
import csv 

data = pd.read_csv('D:/myworkspace/github/movie.csv', encoding='utf-8')
data = data[['TITLE', 'OPEN_DT', 'NAVER_CMT', 'NAVER_CMT_NN', 'PLOT', 'NAVER_PRE_EVAL']]
data = data.dropna()

# data = data[60:65]
# print(data)
# print(type(data))

data = data[0:2]
  
data['NAVER_CMT'] = data['NAVER_CMT'].apply(lambda x : re.sub('[^0-9a-zA-Zㄱ-힗 ]', '', str(x)))
# print(cmt.head())
# print('-'*50)
   
okt = Okt()
def tokenizer_okt_morphs(doc):
    return okt.morphs(doc)
 
data['TOKEN_CMT'] = data['NAVER_CMT'].apply(tokenizer_okt_morphs)
# print(data['TOKEN_CMT'].iloc[0])
# print(data.head())
# print(sentDict.keys())




table = dict() 
with open('D:/myworkspace/github/텍스트분석/polarity.csv', 'r', encoding='utf-8') as polarity: 
    next(polarity) 
    # n gram Negative, Neutrual, Positive 
    for line in csv.reader(polarity): 
        key = str() 
        for word in line[0].split(';'): 
            key += word.split('/')[0] 
            table[key] = {'Neg': line[3], 'Neut': line[4], 'Pos': line[6]} 
            
# print(table['화재'])
# print(type(table))


for token in data['TOKEN_CMT']:
    for word in token: 
        negative = 0
        neutral = 0 
        positive = 0
        if word in table.keys(): 
            negative += int( table[word]['Neg'] )
            neutral += int( table[word]['Neut'] )
            positive += int( table[word]['Pos'] )
        print(word)
        print(negative)
        print(neutral)
        print(positive)
    break
        
    
            





# sentDf.columns = ['word', 'score']
# # print(sentDf.head())
# # print('-'*50)
# sentDict = sentDf.set_index('word')['score'].to_dict()
# # print(sentDict)
# 
# data = pd.read_csv('D:/myworkspace/github/movie.csv', encoding='utf-8')
# data = data[['TITLE', 'OPEN_DT', 'NAVER_CMT', 'NAVER_CMT_NN', 'PLOT', 'NAVER_PRE_EVAL']]
# data = data.dropna()
#  
# # data = data[60:65]
# # print(data)
# # print(type(data))
#  
# data['NAVER_CMT'] = data['NAVER_CMT'].apply(lambda x : re.sub('[^0-9a-zA-Zㄱ-힗 ]', '', str(x)))
# # print(cmt.head())
# # print('-'*50)
#   
# okt = Okt()
# def tokenizer_okt_morphs(doc):
#     return okt.morphs(doc)
# 
#   
# data['TOKEN_CMT'] = data['NAVER_CMT'].apply(tokenizer_okt_morphs)
# # print(data['TOKEN_CMT'].iloc[0])
# # print(data.head())
# # print(sentDict.keys())
#    
# # token : 리스트 / morphs : 한 단어
# # score : 단어의 점수
#   
# print('점수 계산 시작')
#   
# cmtScore = []
# for idx in range( len( data['TOKEN_CMT'] ) ):
#     token = data['TOKEN_CMT'].iloc[idx]
#     cmt_nn = data['NAVER_CMT_NN'].iloc[idx]
#     token = set(token)
#     score = 0
#     for morphs in token : 
#         if morphs in sentDict.keys():
#             score += sentDict[morphs] 
# #     print('score:', score)
# #     print('cmt_nn:', cmt_nn)
# #     print(scoreList)
# #     print(len(scoreList))
#     cmtScore.append(round( score/cmt_nn, 4) )
#        
# print('점수 계산 끝')    
#    
# # print(cmtScore)
#                
#    
# data['CMT_SCORE'] = cmtScore 
#    
# print(data.head())
#    
# data = data[['TITLE', 'OPEN_DT', 'CMT_SCORE']]
#    
# data.to_csv('movie_cmt_score.csv', index = False, header = True, encoding = 'utf-8')
# 
# print('finished')