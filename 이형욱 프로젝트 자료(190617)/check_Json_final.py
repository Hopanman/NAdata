import pandas as pd
from project1906.naver_movie_API_functions import Naver_movie_API
import re
import time

myfile='영진위 전국관객수==1 목록.csv'

viewer1_df=pd.read_csv(myfile,encoding='cp949')

viewer1_list=viewer1_df.values.flatten().tolist()

# print(len(viewer1_list))

file1='(누락 영화 -연도차이 ,무삭제판,감독판 제외 )목록 .csv'

final_noJsonresult=pd.read_csv(file1,encoding='cp949')

final_noJsonresult_list=final_noJsonresult.values.flatten().tolist()

# print(len(final_noJsonresult_list)) #64
# print(final_noJsonresult_list[:10])

for onemovie in viewer1_list:
    if onemovie in final_noJsonresult_list:
        final_noJsonresult_list.remove(onemovie)
 
# print(len(final_noJsonresult_list))#53 관객수1 제외한 리스트 

#########################################
myfile='영진위 영화 개봉일람(2010~2019).csv'

kofic_df=pd.read_csv(myfile,encoding='utf-8')

newdf=pd.DataFrame()
for title in final_noJsonresult_list:
    result=kofic_df.loc[kofic_df['영화명']==title,['영화명','개봉일']]
    newdf=pd.concat([newdf,result])
# print(newdf.head())

# newdf.to_csv('(누락 영화 -연도차이 ,무삭제판,감독판 , 전국관객수==1 제외 )목록 .csv',encoding='cp949',index=False)
# print('(누락 영화 -연도차이 ,무삭제판,감독판 , 전국관객수==1 제외 )목록 .csv 저장 완료')


##########################################
myfile2='(누락 영화 -연도차이 ,무삭제판,감독판 , 전국관객수==1 제외 )목록 .csv'

df_final=pd.read_csv(myfile2,encoding='cp949')

movielist=df_final.loc[df_final['imsi']!='None',['imsi']].values.flatten().tolist()
# print(movielist[:2])
# print(len(movielist))
# print(movielist)


#########################################
no_use_word='[<b>/]'
idx=0
wait=0.125
no_result_list=list()
 
for onemovie in movielist:
    idx+=1
    mymovie=Naver_movie_API(onemovie)
    jsonresult=mymovie.getNaverMovieResult(moviename=onemovie,display=1,yearfrom=1950)
      
    moviedict=jsonresult['items']
#     print(jsonresult)
#     print(len(moviedict))
      
    if len(moviedict)!=0:
        moviedict=moviedict[0]
        mymovie.toJson(jsonresult) 
        title=re.sub(no_use_word,'',moviedict['title'])
        print('{}번째 _{}_제이슨 정보 저장 완료'.format(str(idx).zfill(5),title))
#       
#     else:
#         no_result_list.append(onemovie)
#  
#     time.sleep(wait)
 
print('fin')