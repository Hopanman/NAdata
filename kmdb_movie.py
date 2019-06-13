from urllib.parse import quote
import urllib.request
import json

service_key = '7J3BA5CHYBGW4H91UV78'

def urlRequest(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('크롤링 성공!')
            
            return response.read().decode('utf-8')
    
    except Exception:
        print('크롤링 실패 ㅜㅜ 확인바람')
        
        return None


def testMovie(startdate, enddate, title, detail='N'):
    
    end_point = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json.jsp?'
    
    parameters = 'collection=kmdb_new'
    parameters += '&detail=' + detail
    parameters += '&releaseDts=' + str(startdate)
    parameters += '&releaseDte=' + str(enddate)
    parameters += '&title=' + quote(title)
    parameters += '&ServiceKey=' + service_key
    
    url = end_point + parameters
    
    jsondata = urlRequest(url)
    
    if jsondata == None:
        
        return None
    
    else:
        
        return json.loads(jsondata)


moviedata = testMovie(20140730, 20140730, '명량', detail='Y')


for dataset in moviedata['Data']:
    for moviedata in dataset['Result']:
        
        print('장르:', moviedata['genre'])
        print('-'*40)
        print('개봉일:', moviedata['rating'][-1]['releaseDate'])
        print('-'*40)
        print('영화제목:', moviedata['title'])
        print('-'*40)
        print('제작사:', moviedata['company'])
        print('-'*40)
        print('촬영장소:', moviedata['fLocation'])
        print('-'*40)
        print('런타임:', moviedata['runtime'])
        print('-'*40)
        print('키워드:', moviedata['keywords'])
        print('-'*40)
        print('스크린수:', moviedata['screenCnt'])
        print('-'*40)
        print('매출액:', moviedata['salesAcc'])
        print('-'*40)
        print('관객수:', moviedata['audiAcc'])
        print('-'*40)
        print('관람등급:', moviedata['rating'][-1]['ratingGrade'])
        print('-'*40)
        print('수상내역:', moviedata['Awards1'], moviedata['Awards2'])
        print('-'*40)
        print('줄거리:', moviedata['plot'])
        print('-'*40)
        print('에피소드:', moviedata['episodes'])
        print('-'*40)
        print('감독정보:', moviedata['director'])
        print('-'*40)
        print('배우정보:', moviedata['actor'])
        print('-'*40)
        print('스텝정보:', moviedata['staff'])
        print('-'*40)





