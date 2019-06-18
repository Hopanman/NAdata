import urllib.request
import json
import requests
import pandas as pd
from urllib import parse

######################################################################################
for idx in range(111):
# 영화목록 확인가능 변수
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'
    url += '?key=8ccfd7e4b86fa70f21da9b3bf8cfdc8e'
    url += '&openStartDt=2010'
    url += '&openEndDt=2019'
    url += '&curPage='
    url += str(idx+1)
    url += '&itemPerPage=100'
     
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
     
    if(rescode == 200):
        movieData = json.loads(response.read().decode('utf-8'))
        print(movieData)
        print('-'*40)
    else:
        print("Error code:"+rescode)
         
    moviedf = pd.DataFrame()
    moviedf = moviedf.append(
        {'movieCd':'', 'movieNm':'', 'openDt':'', 'peopleNm':'', 'showTm':'', 'watchGradeNm':'', 'companyNm':'', 'genreNm':''}, ignore_index=True)
     
    num = len(movieData['movieListResult']['movieList'])
    for i in range(0, num):
        moviedf.ix[i,"movieCd"] = movieData["movieListResult"]["movieList"][i]["movieCd"]
        moviedf.ix[i,"movieNm"] = movieData["movieListResult"]["movieList"][i]["movieNm"]
        moviedf.ix[i,"repNationNm"] = movieData["movieListResult"]["movieList"][i]["repNationNm"]
        moviedf.ix[i,"openDt"] = movieData["movieListResult"]["movieList"][i]["openDt"]
    
#     print(moviedf)
    
    ######################################################################################
    
    for i in range(0, num):
        url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
        url += '?key=8ccfd7e4b86fa70f21da9b3bf8cfdc8e'
        url += '&movieCd='
        url += moviedf.ix[i, 'movieCd']
     
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
      
        if(rescode == 200):
            movieData = json.loads(response.read().decode('utf-8'))
            print(movieData)
             
        else:
            print("Error code:"+rescode)
     
        req = requests.get(url)
    #     print(req.json()['movieInfoResult']['movieInfo']['showTm'])
        if req.json()['movieInfoResult'] != []:
            moviedf.ix[i,"showTm"] = req.json()['movieInfoResult']['movieInfo']['showTm']
            if req.json()['movieInfoResult']['movieInfo']['audits'] != []:
                moviedf.ix[i,"watchGradeNm"] = req.json()['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm']
            else:
                moviedf.ix[i, "watchGradeNm"] = ''
        
            
            for onecompany in range(len(req.json()['movieInfoResult']['movieInfo']['companys'])):
                if req.json()['movieInfoResult']['movieInfo']['companys'][onecompany]['companyPartNm'] =='배급사':
                    moviedf.ix[i,"companyNm"] = req.json()['movieInfoResult']['movieInfo']['companys'][onecompany]['companyNm']
        #     print(len(req.json()['movieInfoResult']['movieInfo']['staffs']))
        #     moviedf.ix[i, 'staffs'] = req.json()['movieInfoResult']['movieInfo']['staffs']
        
            genre_list = []
            for onegenre in range(len(req.json()['movieInfoResult']['movieInfo']['genres'])):
                genre_list.append(req.json()['movieInfoResult']['movieInfo']['genres'][onegenre]['genreNm'])
            moviedf.ix[i, 'genreNm'] = genre_list
        
            name_list = []
            role_list = []
            
            for onepeople in range(len(req.json()['movieInfoResult']['movieInfo']['actors'])):
                name_list.append(req.json()['movieInfoResult']['movieInfo']['actors'][onepeople]['peopleNm'])
                role_list.append(req.json()['movieInfoResult']['movieInfo']['actors'][onepeople]['cast'])
             
            for onestaff in range(len(req.json()['movieInfoResult']['movieInfo']['staffs'])):
                name_list.append(req.json()['movieInfoResult']['movieInfo']['staffs'][onestaff]['peopleNm'])
                role_list.append(req.json()['movieInfoResult']['movieInfo']['staffs'][onestaff]['staffRoleNm'])
            people_list = list(zip(name_list, role_list))
        
            
            moviedf.ix[i, "peopleNm"] = people_list
        else:
            moviedf.ix[i,["showTm", 'watchGradeNm', 'companyNm', 'genreNm', 'peopleNm']] = ''
            
            
    print(moviedf)
    
    filename = 'kobisapi_' + str(idx+1) +'.csv'
     
    moviedf.to_csv( filename, encoding = 'utf-8')
    print(filename + '파일로 저장됨')