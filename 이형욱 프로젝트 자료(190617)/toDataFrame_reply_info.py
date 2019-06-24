import numpy as np
import pandas as pd
import time
import re
import os
import json
from pandas import DataFrame


# path='C:/myworkspace/MyPython/project1906/Naver_reply_list/' #누락되지 않은 영화 댓글 파일
path='C:/myworkspace/MyPython/project1906/Naver_ommitted_reply_list/' #누락된 영화 댓글 파일
filelists=os.listdir(path)
# print(filelists[:10])

reply_list=list() #덧글을 저장할 리스트

# json_path='C:/myworkspace/MyPython/project1906/Naver_movie_json/'
json_path='C:/myworkspace/MyPython/project1906/Naver_movie_omitted_json/'
json_lists=os.listdir(json_path)

mycolumn=['영화명','감독','개봉전 평점','총댓글수(개봉전)','댓글모음']
complete_df=pd.DataFrame()
error_list=list() #에러 발생 영화 리스트

# print(filelists[:10])
# print(json_lists[:10])

# imsi_file_list=[re.sub('\s','',imsi_title.split('_')[1]) for imsi_title in filelists]
imsi_list=[re.sub('\s','',imsititle.split('.json')[0]) for imsititle in json_lists] #제이슨 영화 변환 리스트
# print(type(imsi_list))



# ###덧글리스트의 각 파일 별 반복
for onecsv in filelists:
    datalist=list() #데이터를 저장할 리스트
       
       
    title=onecsv.split('_')[1] #영화제목
#     print(title)
      
    onefile=path+onecsv
      
    try:     
        onedf=pd.read_csv(onefile,encoding='utf-8')
        onelist=onedf.values.flatten().tolist()
        all_reply=np.array(onelist[:-2]) #전체 댓글 모음
        all_reply_=''
        for reply in all_reply:
            all_reply_ +=str(reply)
        all_reply=all_reply_
        before_score=onelist[-2].split(':')[1].replace(' ','') #개봉전 평점
        total_reply=onelist[-1].split(':')[1].replace(' ','') #전체 댓글수
      
      
##제이슨 파일 불러오기
 
    ###제이슨 리스트와 덧글 리스트의 제목을 비교해서 동일하면 제이슨 출력 
    
        if re.sub('\s','',title) in imsi_list:
        
            json_idx=(imsi_list.index(re.sub('\s','',title)))
            
            json_title=json_lists[json_idx].split('.json')[0]
#         print(json_lists[json_idx])
#         print(json_title)  
#     ###########
#        
            onejson=json_path + '{}.json'.format(json_title)
         
            rfile=open(onejson,'rt',encoding='utf-8')
            rfile=rfile.read()
            result=json.loads(rfile) #전체 제이슨파일 내용
         
            itemlist=result['items']
            moviedict=itemlist[0] #itemlist속 사전
             
            #     pubdate=moviedict['pubDate']
#             director=moviedict['director'].replace('|',' ')
            director=moviedict['director'].rstrip('|').replace('|',',')  
    # ##리스트에 정보저장하기
    #         
        datalist.append(title)
        #     datalist.append(pubdate)
        datalist.append(director)
        datalist.append(before_score)
        datalist.append(total_reply)
        datalist.append(all_reply)
         
        result_frame=pd.DataFrame(np.reshape(np.array(datalist),(1,5)),index=None,columns=mycolumn)
         
        complete_df=pd.concat([complete_df,result_frame])
   
    except Exception as e:
        print(e)
#         error_list.append(title)
# print(len(complete_df))
 
##완성된 데이터 프레임 저장
  
# complete_df.to_csv('1차 완성본(기존 제이슨 존재 영화).csv',index=None,encoding='utf-8')
complete_df.to_csv('2차 완성본(기존 제이슨 누락 영화).csv',index=None,encoding='utf-8')
print('csv 파일 저장 완료')


### 1,2차 완성본 합치기
# myfile1='1차 완성본(기존 제이슨 존재 영화).csv'
# myfile2='2차 완성본(기존 제이슨 누락 영화).csv'
# 
# df1=pd.read_csv(myfile1,encoding='utf-8')
# df2=pd.read_csv(myfile2,encoding='utf-8')
# 
# final_df=pd.concat([df1,df2])
# 
# final_df.to_csv('최종 네이버 영화 개봉전 댓글 및 평점.csv',encoding='utf-8',index=None)
# print('최종 네이버 영화 개봉전 댓글 및 평점.csv 저장 완료')
   
  
print('fin')

##################################

#     print(datalist)
#     print(pubdate)
#     print(director)
#     print(onejson)
#     print(before_score)
#     print(total_reply)
#     print(title)
#     print(onelist[:2])
#     print(onelist[:-1])

#아이디어
#제목을 뽑음 , json파일을 열고, pubDate(개봉연도),director(감독명)을 가지고옴
#제목, 개봉연도, 감독명, 개봉전 평점, 총댓글수(개봉전), 댓글모음 칼럼으로
#데이터프레임 정리
    
    
    
    
    
    
    
    
    
    
    
#     onejson=path+onestr
# #     print(onejson)
# 
#     rfile=open(onejson,'rt',encoding='utf-8')
#     rfile=rfile.read()
#     result=json.loads(rfile) #전체 제이슨파일 내용
#     # print(result)
#     itemlist=result['items'] #전체 제이슨 중 items 내용 (사전을 갖고 있는 리스트 타입)
# #     print(itemlist) 
#     if len(itemlist)!=0:
#         itemDict=itemlist.pop(0) #리스트에서 사전을 꺼냄
#     # print(itemDict)
#     # print(type(itemDict))
#     
#     # 제목 전환
#         regExp='[<b>/]'   
#         title=itemDict['title']
#         title=re.sub(regExp,'',title)
#         link=itemDict['link'] #해당 영화 링크
#         mylist.append((title,link)) #제목 링크 저장
# #         mylist.append(link) #링크만 저장
#     # print(link)
#     # print(type(link))
#     
#     else:
#         no_dict_list.append(onestr)
# # print(len(mylist))
# # print(len(no_dict_list))
# 
# 
# ###
# #리스트를 csv파일로 저장하기
# myframe=DataFrame(mylist)
#  
# filename='누락되었던 영화 링크모음.csv'
#  
# myframe.to_csv(filename,index=False,encoding='cp949')
#  
# print(filename+'저장 완료되었습니다.')