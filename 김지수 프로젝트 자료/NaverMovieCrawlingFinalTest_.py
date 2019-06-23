# 영진위 영화제목 끌어오기 추가하기

import json
import urllib.request
import datetime

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
        print('[%s] Url Request Success'%(datetime.datetime.now(),url))
        return None

#영화 홈페이지에서 영화명검색
def getNaverMovieResult(moviename,display):
        url='https://openapi.naver.com/v1/search/movie.json'
        url+='?query=%s'%(urllib.parse.quote(moviename))
        url+='&display=%s'%(display)
        url+='&yearfrom=%d'%(2018)
        url+='&yearto=%d'%(2019)
        
        retData = get_request_url(url)
        
        if(retData == None):
            return None
        
        else:
            return json.loads(retData)

jsonResult=list()
movieNm='알라딘'
display_count=100

jsonSearch=getNaverMovieResult(movieNm, display_count)

# print(jsonSearch.items())
result = jsonSearch['items']
print(result)

for movieDict in result:
    movieUrl = movieDict['link']
    print(movieUrl)

 
 
 
 

from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re
   
# 영화 개수 : 10001 ~ 186611 (176,601개)

try:        
    response = urlopen(movieUrl)
          
    soup = BeautifulSoup(response, 'html.parser')
    # print(soup)
       
    ###### 원작 도서 시작 
    # 원작도서 있음 : 1 / 없음 : 0
    myLi = soup.find('a', attrs={'title':'원작 도서'})
    if myLi != None:
        ori_book = myLi.get_text()
        print('원작도서 : 1')
        # print(myLi) 
    else:
        print('원작도서 : 0')  
    ###### 원작 도서 끝
      
    ###### 기대지수 시작
    naver_ex_pt = soup.select_one('span#interest_cnt_basic')
    naver_ex_pt = naver_ex_pt.get_text()
    # print(naver_ex_pt)
    naver_ex_pt = re.sub('[가-히]+','', naver_ex_pt)
    print('기대지수 : %s' % (naver_ex_pt))
    ###### 기대지수 끝
          
except Exception as err :
    print('movieNm : %s 오류' % (movieNm))
    pass
  
  
print('finished')
  


