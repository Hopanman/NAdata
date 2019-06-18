import urllib.request
import json
import datetime
import pandas as pd
import time


from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re


###### 클래스 GetMovieJson
class GetMovieJson:
    ###### API 계정으로 접속
    def get_request_url(self, url):
        self.url = url
        client_id='crz2qOgxFNZE9g3n7Zxg'
        client_secret='ebKzukzImT'
        
        req=urllib.request.Request(self.url)
        req.add_header("X-Naver-Client-Id", client_id)
        req.add_header("X-Naver-Client-Secret",client_secret)
        
        try:
            response=urllib.request.urlopen(req)
            print( '[%s] Url Request Success' % (datetime.datetime.now()) )
            return response.read().decode('utf-8')
        
        except Exception as err:
            print(err)
            print( '[%s] Url Request Fail [url : %s]' % (datetime.datetime.now(), self.url) )
            return None
    
    ###### 네이버 영화 홈페이지에서 영화명 검색
    def getSearchResult(self, movieNm, display):
        self.movieNm = movieNm
        self.display = display
        url='https://openapi.naver.com/v1/search/movie.json'
        url+='?query=%s'%(urllib.parse.quote(self.movieNm))
        url+='&display=%s'%(self.display)
        url+='&yearfrom=%d'%(2010)
        url+='&yearto=%d'%(2019)
        
        retData = self.get_request_url(url)
        
        if(retData == None):
            return None
        else:
            return json.loads(retData)
###### 클래스 GetMovieJson

###### 클래스 GetMovieJson
class GetMovieList:
    ###### KOFIC 영화명, 감독명 추출
    def getKoficData(self, filename):
        self.filename = filename
        
        koficData = pd.read_csv(self.filename)
        koficData.fillna('NaN', inplace=True)
        # print(koficData)
        
        koficNmDr = koficData[['영화명', '감독']]
        # print(koficNmDr)
        # print(type(koficNmDr))
        jsonList = self.getNaverJson(koficNmDr)
        return jsonList
    
    ###### 영화리스트 : [kofic영화명, kofic감독, GetMovieJson검색결과]
    def getNaverJson(self, dataframe):
        self.dataframe = dataframe 
        MovieJson = GetMovieJson()
        length = len(self.dataframe)
        jsonList = []
        
        for idx in range(length):
        # for idx in range(20,30):
            koficNm = self.dataframe.iloc[idx, 0]
            koficDr = self.dataframe.iloc[idx, 1]
            koficDr = koficDr.split(',')
            # print(idx)
            # print(koficNm)
            # print(koficDr)
            # print('-'*50)
            
            getJson = GetMovieJson()
                     
            display_count=100
             
            ###### Naver API에서 해당 영화명 검색 결과 추출 Start    
            naverJson=getJson.getSearchResult(koficNm, display_count)
            jsonList.append([koficNm, koficDr, naverJson])
            # print(naverJson) 
            # print('#'*50)  
               
            # HTTP Error 429: Too Many Requests
            # 에러를 방지하기 위한 시간차 
            time.sleep(0.5)
            ###### Naver API에서 해당 영화명 검색 결과 추출 End
        # print(jsonList)
        return jsonList
    
    def getNaverUrl(self, filename):
        self.filename = filename
        jsonList = self.getKoficData(self.filename)
        # print(jsonList)
    
        UrlList = []
        
        for oneJson in jsonList:
            koficNm = oneJson[0]
            koficDr = oneJson[1]
            naverJson = oneJson[2]
            naverJsonList = naverJson['items']     
            # print(naverJsonList)
            
            for naverJson in naverJsonList:
                naverNm = naverJson['title'].replace('<b>','').replace('</b>','')
                naverDr = naverJson['director'].replace('<b>','').replace('</b>','')
                naverDr = naverDr.rstrip('|').split('|')
                       
                if naverNm == koficNm:
                    if naverDr == koficDr:
                        naverUrl = naverJson['link'] 
                        UrlList.append([naverNm, naverDr, naverUrl])
                        # print([koficNm, naverNm, koficDr, naverDr, naverUrl])           
                    else:
                        # print('감독 다름') 
                        # print([koficNm, naverNm, koficDr, naverDr])
                        pass
                    ############# ** 해외 감독의 경우 한글표기가 다르게 되어서 안 나오는 경우 있음 (아이언맨3 : 셰인 블랙 / 쉐인 블랙)
                    ############# 나중에 영진위에서 영화 영문 제목 가져와서 비교해도 괜찮을 것 같음
                        # if naverDr[0][0:2] == koficDr[0][0:2]:
                            # naverUrl = naverJson['link'] 
                            # print([koficNm, naverNm, koficDr, naverDr, naverUrl])  
                        # elif naverDr[0][-2:] == koficDr[0][-2:]:
                            # naverUrl = naverJson['link'] 
                            # print([koficNm, naverNm, koficDr, naverDr, naverUrl])
                        # else :
                            # print('감독 다름') 
                            # print([koficNm, naverNm, koficDr, naverDr])
                            # pass
                    ############## ** 검색결과가 많이 나오는 경우 해당 영화가 아예 안나오기도 함.(아바타 : 제임스 카메론 => 다른 영화만 나옴) 
                    ############## 링크를 10000부터 숫자로 하는 것도 고려해봐야할 듯.           
                else :
                    # print('제목 다름')
                    # print([koficNm, naverNm, koficDr, naverDr])
                    pass 
                 
                # print('-'*50)
            # print('#'*50)
         
        return UrlList   # UrlList : [[naverNm, naverDr, naverUrl], ... ]

class Get_Oribook_Expt:
    def getOribookExpt(self, filename):
        self.filename = filename
        
        getList = GetMovieList()
        
        urlList = getList.getNaverUrl(self.filename)
        
        oribook_exptList = []
        urlCnt = len(urlList)
        
        for idx in range(urlCnt):
            movieNm = urlList[idx][0]
            movieDr = urlList[idx][1]
            movieUrl = urlList[idx][2]

            response = urlopen(movieUrl)
                  
            soup = BeautifulSoup(response, 'html.parser')
            # print(soup)
                           
            ###### 원작 도서 시작 
            # 원작도서 있음 : 1 / 없음 : 0
            myLi = soup.find('a', attrs={'title':'원작 도서'})
            if myLi != None:
                oribook = 1
            else:
                oribook = 0
            # print('원작도서 : %d' % (oribook))
            ###### 원작 도서 끝
                           
            ###### 기대지수 시작
            naver_ex_pt = soup.select_one('span#interest_cnt_basic')
            naver_ex_pt = naver_ex_pt.get_text()
            naver_ex_pt = re.sub('[가-히]+','', naver_ex_pt)
            naver_ex_pt = naver_ex_pt.replace(',','')
            naver_ex_pt = int(naver_ex_pt)
            # print('기대지수 : %d' % (naver_ex_pt))
            ###### 기대지수 끝
            
            oribook_exptList.append([movieNm, movieDr, movieUrl, oribook, naver_ex_pt])
            
        self.saveToCsv(oribook_exptList, 'Naver_Oribook_Expt.csv')
        return([movieNm, movieDr, movieUrl, oribook, naver_ex_pt])
            
    def saveToCsv(self, listname, newfilename):
        self.listname = listname 
        self.newfilename = newfilename
        Oribook_exptDf = pd.DataFrame(self.listname, columns=['movieNm', 'movieDr', 'naverUrl', 'ori_book', 'naver_ex_pt'])
        # print(Oribook_exptDf)
        Oribook_exptDf.to_csv(self.newfilename, header=True, index = False, encoding='utf-8')
        




       
    
