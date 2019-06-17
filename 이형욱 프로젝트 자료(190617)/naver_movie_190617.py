import json
import urllib.request
import datetime
import pandas as pd 
import time

##api계정으로 접속
def get_request_url(url):
    client_id='sQ_53I11un7a4GN_0E_v'
    client_secret='BylBuZooyk'
    
    req=urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)
    try:
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
            print('[%s] Url Request Success'%(datetime.datetime.now()))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
#         print(url)##190617
        print('[%s] Url Request Success'%(datetime.datetime.now(),url))
        return None

#영화 홈페이지에서 영화명검색
def getNaverMovieResult(moviename,display):
        no_use_words=(' / ,:, * ,?, " ,<, >, |')
        url='https://openapi.naver.com/v1/search/movie.json'
        url+='?query=%s'%(urllib.parse.quote(moviename.replace(no_use_words,'')))
        url+='&display=%s'%(display)
        url+='&yearfrom=%d'%(2010)
        url+='&yearto=%d'%(2019)
        
        retData = get_request_url(url)
        
        if(retData == None):
            return None
        
        else:
            return json.loads(retData)

###API에서 불러온 정보 json파일로 저장
def toJson(result):
    with open('C:/myworkspace/MyPython/project1906/Naver_movie_json/{}.json'.format(save_name.replace((' / ,:, * ,?, " ,<, >, |'),'')), 'w', encoding='utf-8') as file :
        json.dump(result, file, ensure_ascii=False, indent='\t')


###
#영진위 목록은 KOFIC_API클래스에서 csv로 저장
myfile='영진위 영화 개봉일람(2010~2019).csv'
df=pd.read_csv(myfile,encoding='utf-8')
movielist=df.loc[:,'영화명'] #영화이름만 정리된 배열 (Series type)
# print(movielist) 
# print(type(movielist))
# print(movielist[89])
# print(type(movielist[89]))
# print(movielist.values[0:20])
# movielist=['알라딘'] #시험용 예제
# print(movielist.shape) 10465개
# print(int((movielist.shape[0])/20))
# print(movielist.values)

###무비리스트 20개 단위로 자르기
len20_lists=list()
list_no=int((movielist.shape[0])/20) #전체 리스트 갯수
for idx in range((list_no)+1): #idx :0-523 (0:524)
    #[0:20],[20:40],[40:60], ... ,[10460:10480]
    imsi=movielist.values[idx*20:(idx+1)*20].tolist()
    len20_lists.append(imsi)
# print(type(len20_lists))
# print(len(len20_lists))
# print(type(len20_lists[-2]))
# print(len20_lists[4]) #예시용 5개만.


### 네이버 api에서 정보 불러와서 json 파일 저장

#예시용(5개만 불러와서 저장)
no_use_words=(' / ,:, * ,?, " ,<, >, |')
display_count=1
count=0
for m_list in len20_lists[22:25]:  #2번 실행됨
    count+=1    
    for m_name in m_list:   #20번 실행
        wait=0.125
        m_index=m_list.index(m_name)+1
         
        save_name=m_name.replace(no_use_words,'')
            
        jsonSearch=getNaverMovieResult(save_name, display_count)
        toJson(jsonSearch)
        time.sleep(wait)#429오류 방지(naver api오류)
         
         
        print('{}번 리스트 {}번째 영화 {}.json 파일 저장 완료되었습니다'.format(count,m_index,save_name))
        print('{}초 동안 대기합니다'.format(wait))

##리스트로 20개씩 저장하기
# no_use_words=(' / ,:, * ,?, " ,<, >, |')
# display_count=1
# count=0  
# for m_list in len20_lists[22:]:  #524번 실행됨
#     count+=1
#     for m_name in m_list:   #20번 실행
#         wait=0.125
#         m_index=m_list.index(m_name)+1
#   
#         save_name=m_name.replace(no_use_words,'')
#            
#         jsonSearch=getNaverMovieResult(save_name, display_count)
#         toJson(jsonSearch)
#         time.sleep(wait)#429오류 방지(naver api오류)
#         
#         
#         print('{}번 리스트 {}번째 영화 {}.json 파일 저장 완료되었습니다'.format(count,m_index,save_name))
#         print('{}초 동안 대기합니다'.format(wait))
        


##각 영화마다 저장하는 코드
# display_count=1
#  
# for m_name in movielist:
#     jsonSearch=getNaverMovieResult(m_name, display_count)
#     toJson(jsonSearch)
#     print('{}.json 파일 저장 완료되었습니다'.format(m_name))
    
# print(jsonSearch.items())
# print(jsonSearch['items'])