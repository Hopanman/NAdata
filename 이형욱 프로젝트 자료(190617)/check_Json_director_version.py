import pandas as pd
from project1906.naver_movie_API_functions import Naver_movie_API
import re
import time

myfile='(누락 영화-연도차이 ,무삭제판 제외,전국관객수==1제외)중 감독판 목록_imsi .csv'
df=pd.read_csv(myfile,encoding='cp949')
movielist=df.loc[df['imsi']!='None',['imsi']]

# print(df.head())
# print(df['imsi'][0])
# print(type(df['imsi'][0]))
# print(df.loc[df['imsi']!='None',['imsi']])
# print(movielist.head())

movielist=movielist.values.flatten().tolist()
# print(movie)
# print(type(movielist))
     
##################################
no_use_word='[<b>/]'
idx=0
wait=0.125
no_result_list=list()
 
for onemovie in movielist:
    idx+=1
    mymovie=Naver_movie_API(onemovie)
    jsonresult=mymovie.getNaverMovieResult(onemovie,1,1950)
#      
    moviedict=jsonresult['items']
#      
    if len(moviedict)!=0:
        moviedict=moviedict[0]
        mymovie.toJson(jsonresult) 
        title=re.sub(no_use_word,'',moviedict['title'])
        print('{}번째 _{}_제이슨 정보 저장 완료'.format(str(idx).zfill(5),title))
#      
    else:
        no_result_list.append(onemovie)
# 
    time.sleep(wait)
# data=pd.DataFrame(no_result_list)
# data.to_csv('누락영화리스트(현지와 우리나라 개봉차이 제외 ).csv',
#             encoding='cp949',index=False)
# print('누락 영화리스트 저장 완료')
print('fin')