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
moviename='알라딘'
display_count=100

jsonSearch=getNaverMovieResult(moviename, display_count)

# print(jsonSearch.items())
print(jsonSearch['items'])