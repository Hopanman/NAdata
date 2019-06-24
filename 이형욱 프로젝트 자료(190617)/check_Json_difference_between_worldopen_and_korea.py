import pandas as pd
from project1906.naver_movie_API_functions import Naver_movie_API
import re
import time

myfile='사전누락영화 목록.csv'
df=pd.read_csv(myfile,encoding='utf-8')
movielist=df.values.tolist()
# print(movielist)
# print(type(movielist))

newlist=list()
for idx,title in movielist:
    new_title=title.replace('.json','')
    newlist.append(new_title)
# print(len(newlist))    #1329개
# print(newlist[:10])
# print(type(newlist))

viewer_1='영진위 전국관객수==1 목록.csv'
v1_df=pd.read_csv(viewer_1,encoding='cp949')
v1_list=v1_df.values.flatten().tolist()
# print(v1_list[:4])

for onemovie in v1_list:
    if onemovie in newlist:
        newlist.remove(onemovie) 
# print(len(newlist)) #전국관객수 1 제외후 975개

#########################################

# no_use_word='[<b>/]'
# mymovie=Naver_movie_API('007 북경특급 2') #클래스 객체
# jsonresult=mymovie.getNaverMovieResult('007 북경특급 2',1,1950)
# m_dict=jsonresult['items']
# m_dict=m_dict.pop(0)

# print(jsonresult['items'])
# print(len(jsonresult['items']))
# print(len(mymovie))
# print(m_dict.pop(0))
# print(m_dict['title'])
# print(re.sub(no_use_word,'',m_dict['title']))

#####################
no_use_word='[<b>/]'
idx=0
wait=0.125
no_result_list=list()
 
for onemovie in newlist:
    idx+=1
    mymovie=Naver_movie_API(onemovie)
    jsonresult=mymovie.getNaverMovieResult(moviename=onemovie,display=1,yearfrom=1950)
      
    moviedict=jsonresult['items']
      
    if len(moviedict)!=0:
        moviedict=moviedict[0]
        mymovie.toJson(jsonresult) 
        title=re.sub(no_use_word,'',moviedict['title'])
        print('{}번째 _{}_제이슨 정보 저장 완료'.format(str(idx).zfill(5),title))
      
    else:
        no_result_list.append(onemovie)
 
    time.sleep(wait)

# data=pd.DataFrame(no_result_list)
# data.to_csv('누락영화리스트(현지와 우리나라 개봉차이 제외 ).csv',
#             encoding='cp949',index=False)
# print('누락 영화리스트 저장 완료')
print('fin')
        