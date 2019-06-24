import pandas as pd
from project1906.naver_movie_API_functions import Naver_movie_API
import requests
from bs4 import BeautifulSoup
import time

##감독판 필터링
myfile='(누락 영화 -연도차이 ,무삭제판 제외 )목록 .csv' 

newlist=pd.read_csv(myfile,encoding='cp949')
newlist=newlist.values.flatten().tolist()

other_problem=list()
director_ver=list()
for onemovie in newlist:
    if '감독판' in onemovie:
        director_ver.append(onemovie)
     
    else:
        other_problem.append(onemovie)
     
# print(director_ver)
# print(len(director_ver)) #449
 
# print(other_problem)
# print(len(other_problem)) #123

data=pd.DataFrame(director_ver)
data.to_csv('(누락 영화-연도차이 ,무삭제판 제외)중 감독판 목록 .csv',encoding='cp949',index=False)
print('(누락 영화-연도차이 ,무삭제판 제외)중 감독판 목록 .csv 저장 완료')
 
data=pd.DataFrame(other_problem)
data.to_csv('(누락 영화 -연도차이 ,무삭제판,감독판 제외 )목록 .csv',encoding='cp949',index=False)
print('(누락 영화 -연도차이 ,무삭제판,감독판 제외 )목록 .csv 저장 완료')
