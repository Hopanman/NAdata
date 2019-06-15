from urllib.parse import quote
import urllib.request
import json
from pandas import DataFrame
from json import JSONDecodeError
import re

service_key = ''


def urlRequest(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('크롤링 성공!')
            
            return response.read().decode('utf-8')
    
    except Exception as e:
        print('크롤링 실패 ㅜㅜ', e, '확인바람')
        
        return None

def movieExtractor(startdate, enddate, count):
    
    end_point = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json.jsp?'
    
    parameters = 'collection=kmdb_new'
    parameters += '&detail=Y'
    parameters += '&listCount=1'
    parameters += '&startCount=' + str(count)
    parameters += '&sort=title'
    parameters += '&releaseDts=' + str(startdate)
    parameters += '&releaseDte=' + str(enddate)
    parameters += '&ServiceKey=' + service_key
    
    url = end_point + parameters
    
    jsondata = urlRequest(url)
    
    if jsondata == None:
        
        return None
    
    else:
        try:
            return json.loads(jsondata)
        except JSONDecodeError as e:
            print(e)
            print('JSON데이터에 문제가 있습니다 직접 확인해주세요!')
            return None

def kmdbValueSearcher(year, index, *keys):
    
    end_point = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json.jsp?'
    
    parameters = 'collection=kmdb_new'
    parameters += '&detail=Y'
    parameters += '&listCount=1'
    parameters += '&startCount=' + str(index-1)
    parameters += '&sort=title'
    parameters += '&releaseDts=' + str(year) + '0101'
    parameters += '&releaseDte=' + str(year) + '1231'
    parameters += '&ServiceKey=' + service_key
    
    url = end_point + parameters
    
    data = urlRequest(url)
    
    if data == None:
        
        return None
    else:
        valuelist = list()
        for key in keys:
            match = re.search('"%s":".*?"'%(key),data)
            value = re.search(':".*?"',match.group()).group().strip(':"')
            valuelist.append(value)
            
        return valuelist


yearlist = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
startdate = '0101'
enddate = '0609'
movielist=list()
columns = ['개봉연도','영화제목','키워드','수상내역']


for year in yearlist:
    for idx in range(1000):
        power = True
        print('%s년 %d번째 영화'%(year, idx+1))
        
        if year == '2019':
            moviedata = movieExtractor(int(year+startdate), int(year+enddate), idx)
        else:
            moviedata = movieExtractor(int(year+'0101'), int(year+'1231'), idx)
        try:
            for moviedict in moviedata['Data']:
            
                if moviedict['Result']:
                    for resultdict in moviedict['Result']:
                        movielist.append([int(year), resultdict['title'], resultdict['keywords'], resultdict['Awards1']+'|'+resultdict['Awards2']])

                else:
                    power = False
                    break
        
            if not power:
                break
        except TypeError as e:
            print(e)


errorlist = ['2015년123','2015년362','2015년741','2016년515','2017년838','2018년432','2018년653']


for error in errorlist:
    intargs = error.split('년')
    valuelist = kmdbValueSearcher(int(intargs[0]), int(intargs[1]), 'title', 'keywords', 'Awards1', 'Awards2')
    movielist.append([int(intargs[0]), valuelist[0], valuelist[1], valuelist[2]+'|'+valuelist[3]])


movietable = DataFrame(movielist, columns=columns)
movietable = movietable.sort_values('영화제목')
movietable['영화제목'] = movietable['영화제목'].apply(lambda x: x.strip())
movietable['수상내역'] = movietable['수상내역'].apply(lambda x: x.strip('|'))
movietable = movietable.reindex(['영화제목','개봉연도','키워드','수상내역'], axis=1)
movietable.to_csv('KMDB변수.csv', index=False, encoding='utf-8')

