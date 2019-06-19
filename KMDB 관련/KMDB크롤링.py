import urllib.request
import json
import pandas as pd
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
            
            if key == 'rating':
                value = eval(re.search('(?<="%s":)\[.*?\]'%(key), data).group())
                valuelist.append(value)
            else:
                match = re.search('"%s":".*?"'%(key),data)
                value = re.search(':".*?"',match.group()).group().strip(':"')
                valuelist.append(value)
            
        return valuelist


yearlist = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
startdate = '0101'
enddate = '0609'
movielist=list()
columns = ['개봉일','영화제목','키워드','수상내역']


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
                        for ratingdata in resultdict['rating']:
                            
                            if ratingdata['ratingMain'] == 'Y':
                                rel_data = ratingdata['releaseDate']
                                break
                                
                        movielist.append([rel_data, resultdict['title'], resultdict['keywords'], resultdict['Awards1']+'|'+resultdict['Awards2']])

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
    valuelist = kmdbValueSearcher(int(intargs[0]), int(intargs[1]), 'rating', 'title', 'keywords', 'Awards1', 'Awards2')
    
    for err_ratingdata in valuelist[0]:
        
        if err_ratingdata['ratingMain'] == 'Y':
            err_rel_data = err_ratingdata['releaseDate']
            break
            
    movielist.append([err_rel_data, valuelist[1], valuelist[2], valuelist[3]+'|'+valuelist[4]])


movietable = DataFrame(movielist, columns=columns)
movietable = movietable.sort_values('영화제목')
movietable['영화제목'] = movietable['영화제목'].apply(lambda x: x.strip())
movietable['수상내역'] = movietable['수상내역'].apply(lambda x: x.strip('|'))
movietable = movietable.reindex(['영화제목','개봉일','키워드','수상내역'], axis=1)


movietable.loc[7258,'개봉일'] = '20190425'
movietable.loc[6006,'개봉일'] = '20170828'
movietable.loc[7247,'개봉일'] = None
movietable.loc[5970,'개봉일'] = '20170921'
movietable.loc[4198,'개봉일'] = None
movietable.loc[6743,'개봉일'] = '20180531'
movietable.loc[6727,'개봉일'] = '20180530'
movietable.loc[5920,'개봉일'] = None
movietable.loc[6718,'개봉일'] = None
movietable.loc[4154,'개봉일'] = None
movietable.loc[7211,'개봉일'] = None
movietable.loc[6710,'개봉일'] = '20181105'
movietable.loc[6701,'개봉일'] = '20180802'
movietable.loc[7202,'개봉일'] = None
movietable.loc[6686,'개봉일'] = None
movietable.loc[6677,'개봉일'] = '20180912'
movietable.loc[6674,'개봉일'] = '20180720'
movietable.loc[3248,'개봉일'] = None
movietable.loc[7191,'개봉일'] = None
movietable.loc[5827,'개봉일'] = '20180329'
movietable.loc[7173,'개봉일'] = None
movietable.loc[6642,'개봉일'] = '20180220'
movietable.loc[5758,'개봉일'] = '20170928'
movietable.loc[7145,'개봉일'] = None
movietable.loc[6615,'개봉일'] = None
movietable.loc[6613,'개봉일'] = None
movietable.loc[6594,'개봉일'] = '20180713'
movietable.loc[7133,'개봉일'] = None
movietable.loc[5705,'개봉일'] = None
movietable.loc[5695,'개봉일'] = '20180628'
movietable.loc[7104,'개봉일'] = None
movietable.loc[5634,'개봉일'] = '20170921'
movietable.loc[7079,'개봉일'] = None
movietable.loc[6471,'개봉일'] = None
movietable.loc[6469,'개봉일'] = None
movietable.loc[6466,'개봉일'] = '20180718'
movietable.loc[7061,'개봉일'] = None
movietable.loc[6461,'개봉일'] = '20181025'
movietable.loc[6459,'개봉일'] = '20180906'
movietable.loc[6455,'개봉일'] = None
movietable.loc[6434,'개봉일'] = '20180530'
movietable.loc[6430,'개봉일'] = '20180803'
movietable.loc[7040,'개봉일'] = '20190314'
movietable.loc[6409,'개봉일'] = '20181011'
movietable.loc[7027,'개봉일'] = None
movietable.loc[6400,'개봉일'] = '20181025'
movietable.loc[5480,'개봉일'] = '20170906'
movietable.loc[5470,'개봉일'] = '20170921'
movietable.loc[6383,'개봉일'] = None
movietable.loc[6999,'개봉일'] = None
movietable.loc[6366,'개봉일'] = '20180802'
movietable.loc[6992,'개봉일'] = None
movietable.loc[6985,'개봉일'] = None
movietable.loc[6345,'개봉일'] = '20180906'
movietable.loc[6327,'개봉일'] = '20180829'
movietable.loc[6973,'개봉일'] = None
movietable.loc[6962,'개봉일'] = None
movietable.loc[6297,'개봉일'] = '20180628'
movietable.loc[6951,'개봉일'] = None
movietable.loc[6285,'개봉일'] = None
movietable.loc[6930,'개봉일'] = None
movietable.loc[6236,'개봉일'] = '20180920'
movietable.loc[6223,'개봉일'] = None
movietable.loc[6909,'개봉일'] = None
movietable.loc[5239,'개봉일'] = None
movietable.loc[6207,'개봉일'] = None
movietable.loc[5237,'개봉일'] = None
movietable.loc[6902,'개봉일'] = None
movietable.loc[6194,'개봉일'] = '20181002'
movietable.loc[6193,'개봉일'] = '20180902'
movietable.loc[6891,'개봉일'] = None
movietable.loc[6172,'개봉일'] = '20181228'
movietable.loc[6145,'개봉일'] = '20180613'
movietable.loc[6141,'개봉일'] = '20180704'
movietable.loc[5159,'개봉일'] = '20170921'
movietable.loc[4312,'개봉일'] = None
movietable.loc[6857,'개봉일'] = None
movietable.loc[6851,'개봉일'] = None
movietable.loc[6108,'개봉일'] = '20180828'
movietable.loc[6103,'개봉일'] = None
movietable.loc[6099,'개봉일'] = '20181108'
movietable.loc[6835,'개봉일'] = None
movietable.loc[6093,'개봉일'] = '20180829'
movietable.loc[3456,'개봉일'] = '20150625'
movietable.loc[6063,'개봉일'] = '20180620'
movietable.loc[6060,'개봉일'] = '20180708'
movietable.loc[6041,'개봉일'] = None


movietable.loc[4040,'개봉일'] = '20150618'
movietable.loc[4416,'개봉일'] = '20161201'


movietable.loc[1012,'개봉일'] = '20120801'
movietable.loc[994,'개봉일'] = None
movietable.loc[6730,'개봉일'] = None
movietable.loc[1597,'개봉일'] = None
movietable.loc[413,'개봉일'] = '20140628'
movietable.loc[971,'개봉일'] = None
movietable.loc[1543,'개봉일'] = '20120510'
movietable.loc[1542,'개봉일'] = '20120906'
movietable.loc[1470,'개봉일'] = None
movietable.loc[1465,'개봉일'] = '20120726'
movietable.loc[6580,'개봉일'] = None
movietable.loc[6577,'개봉일'] = None
movietable.loc[6573,'개봉일'] = '20180517'
movietable.loc[1442,'개봉일'] = '20120712'
movietable.loc[1440,'개봉일'] = None
movietable.loc[1430,'개봉일'] = None
movietable.loc[6523,'개봉일'] = '20180524'
movietable.loc[2173,'개봉일'] = '20130204'
movietable.loc[1405,'개봉일'] = None
movietable.loc[2078,'개봉일'] = '20130221'
movietable.loc[1351,'개봉일'] = '20120712'
movietable.loc[6406,'개봉일'] = None
movietable.loc[6401,'개봉일'] = None
movietable.loc[1319,'개봉일'] = '20121129'
movietable.loc[198,'개봉일'] = None
movietable.loc[3701,'개봉일'] = None
movietable.loc[6293,'개봉일'] = '20180613'
movietable.loc[167,'개봉일'] = '20100211'
movietable.loc[662,'개봉일'] = '20121213'
movietable.loc[160,'개봉일'] = None
movietable.loc[6210,'개봉일'] = '20180410'
movietable.loc[103,'개봉일'] = None
movietable.loc[99,'개봉일'] = None
movietable.loc[1137,'개봉일'] = None
movietable.loc[1133,'개봉일'] = '20121122'
movietable.loc[1111,'개봉일'] = None
movietable.loc[31,'개봉일'] = None
movietable.loc[30,'개봉일'] = None
movietable.loc[1078,'개봉일'] = None


movietable['개봉일'] = pd.to_datetime(movietable['개봉일'])
movietable.info()
movietable.to_csv('KMDB변수.csv', index=False, encoding='utf-8')

