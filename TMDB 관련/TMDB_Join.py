import pandas as pd
import datetime
import numpy as np
import re

### Kofic
KoficData = pd.read_csv('kobisapiresult.csv') 
print(KoficData.columns)
print('-'*50)

KoficData = KoficData.iloc[:, 1:]

# KoficData['movieNm'] = KoficData['movieNm'].str.replace('[\W]+','')
# KoficData['movieNm'] = KoficData['movieNm'].str.lower()
# print(KoficData['movieNm'])

KoficData['movieNmEn'] = KoficData['movieNmEn'].str.replace('[\W]+','')
KoficData['movieNmEn'] = KoficData['movieNmEn'].str.lower()
# print(KoficData['movieNmEn'])

# print(KoficData.head(10))
# print('-'*50)

print(KoficData.info())
print('-'*50)
### Kofic


### TMDB 
TMDBData = pd.read_excel('TMDB_revision(excel).xlsx ')
# print(TMDBData.columns)
TMDBData = TMDBData.iloc[:,:10]
TMDBData['openDt'] = TMDBData['openDt'].astype('object')
TMDBData['openDt'] = TMDBData['openDt'].replace(' 00:00:00', '')
TMDBData['openDt'] = TMDBData['openDt'].replace('-', '')
# print(TMDBData['openDt'])
# print('-'*50)
 
# TMDBData['movieNm'] = TMDBData['movieNm'].str.replace('[\W]+','')
# TMDBData['movieNm'] = TMDBData['movieNm'].str.lower()
# print(TMDBData['movieNm'])
 
TMDBData['movieNmEn'] = TMDBData['movieNmEn'].str.replace('[\W]+','')
TMDBData['movieNmEn'] = TMDBData['movieNmEn'].str.lower()
# print(TMDBData['movieNmEn'])
 
# print(TMDBData.head(10))
# print('-'*50)


    
print(TMDBData.info())
print('-'*50)


print(TMDBData[TMDBData['movieNmEn'] == ''])

### TMDB 
    
# innerJoin = pd.merge(KoficData, TMDBData, on = ['movieNmEn'], how='inner', suffixes = ('Kofic', 'TMDB'), indicator=True)
# # print(innerJoin)
# # print('-'*50)
# print(innerJoin.info())
# print('-'*50)
# innerJoin.to_csv('Kofic_TMDB_innerJoin_En.csv', header=True, index = False, encoding='utf-8')
#      
# # print(innerJoin['_merge'].unique())
#    
#    
# outerJoin = pd.merge(KoficData, TMDBData, on = ['movieNmEn'], how='outer', suffixes = ('Kofic', 'TMDB'), indicator=True)
# # print(outerJoin)
# # print('-'*50)
#    
# notJoin = outerJoin[ outerJoin['_merge'] != 'both' ]
# # print(notJoin['_merge'].unique())
# print(notJoin.info())
# print('-'*50)
# notJoin.to_csv('Kofic_TMDB_notJoin_En.csv', header=True, index = False, encoding='utf-8')
#      
# # print(innerJoin['_merge'].unique())
#    
#   
#   
# print('finished')

