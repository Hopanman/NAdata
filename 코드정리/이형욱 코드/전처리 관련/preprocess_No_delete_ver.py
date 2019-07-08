import pandas as pd
from project1906.naver_movie_API_functions import Naver_movie_API
import requests
from bs4 import BeautifulSoup
import time

myfile='누락영화리스트(현지와 우리나라 개봉차이 제외 ).csv' 

newlist=pd.read_csv(myfile,encoding='cp949')
newlist=newlist.values.flatten().tolist()

# print(newlist[:10])
# print(type(newlist))
# print(len(newlist))


##무삭제판 필터링
other_problem=list()
no_delete_ver=list()
for onemovie in newlist:
    if '무삭제' in onemovie:
        no_delete_ver.append(onemovie)
     
    else:
        other_problem.append(onemovie)
    
# print(no_delete_ver)
# print(len(no_delete_ver)) #449

# print(other_problem)
# print(len(other_problem)) #123

data=pd.DataFrame(no_delete_ver)
data.to_csv('(누락 영화-연도차이 제외)중 무삭제판 목록 .csv',encoding='cp949',index=False)
print('(누락 영화-연도차이 제외)중 무삭제판 목록 .csv 저장 완료')
 
data=pd.DataFrame(other_problem)
data.to_csv('(누락 영화 -연도차이 ,무삭제판 제외 )목록 .csv',encoding='cp949',index=False)
print('(누락 영화 -연도차이 ,무삭제판 제외 )목록 .csv 저장 완료')

#######################################

###네이버 무삭제 검색 영화제목 뽑아오기

##전체 페이지수 구하기
link='https://movie.naver.com/movie/search/result.nhn?section=movie&query=%B9%AB%BB%E8%C1%A6&page=1'
 
resp=requests.get(link)
html=BeautifulSoup(resp.content,'html.parser')
 
search_header=html.find('div',{'class':'search_header'})
span_class_number=search_header.find('span',{'class':'num'}).getText()    
 
# print(html)
# print(search_header)
# print(total_page_number)
 
imsi=span_class_number.split('/')
# print(imsi[1])
imsi=imsi[1].split('건')
# print(imsi[0])
total_movie_number=imsi[0].replace(' ','')
# print(total_movie_number)
# print(type(total_movie_number))
 
total_page_number=int(int(total_movie_number)/10)+1
# print(total_page_number)
# print(type(total_page_number))
 
###########################################

##무삭제 검색결과 csv저장하기

wait=0.125
search_result=list()
for idx in range(total_page_number): #0-6
    link='https://movie.naver.com/movie/search/result.nhn?section=movie&query=%B9%AB%BB%E8%C1%A6&page={}'.format(idx+1)
#     print(link)
     
    resp=requests.get(link)
    html=BeautifulSoup(resp.content,'html.parser')
    search_list=html.find('ul',{'class':'search_list_1'})
    lis=search_list.findAll('li')
 
    for li in lis:
        title=li.find('dt').getText()
        search_result.append(title)
    time.sleep(wait)
#         print(title)
# print(lis)
# print(lis[0].find('a').GetText())
data=pd.DataFrame(search_result)
data.to_csv('네이버 영화 무삭제 검색결과.csv',encoding='utf-8',index=False)
print('네이버 영화 무삭제 검색결과.csv 저장완료')

print('fin')

#########################################
# match_list=list()
# no_match_list=list()
# for movie in no_delete_ver:
#     if movie in search_result:
#         match_list.append(movie)
#     else:
#         no_match_list.append(movie)
# 
# print(match_list)
