import http.client
import json


payload = "{}"
TMDBData = []

# page 맥시멈 : 1000
# 개봉일자가 신뢰도가 떨어진 영화가 많아서 현재까지 한국에서 개봉한 모든 영화를 크롤링하는 코드를 작성했습니다.
for idx in range(1000):
    mainUrl = "/3/discover/movie?page="
    mainUrl += str(idx+1) 
    mainUrl += "&include_video=true&include_adult=true&sort_by=original_title.asc&language=ko-KR&region=KR&api_key=2b4a725a283b9fa435aca3507c61bae2"
    
    try:
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        conn.request("GET", mainUrl, payload)
        main_res = conn.getresponse()
        if main_res.getcode() == 200:
            print('Connected!')
            json_main = json.loads(main_res.read().decode('utf-8'))
       
    except Exception as e:
        print('Access failed.', e)
        continue

    movieList = json_main['results']
    

 
    for onemovie in movieList:
#         print(onemovie)
# #         print(onemovie.keys())
        id = onemovie['id']
        title = onemovie['title']
#         print(id)
#         print(title)
#         print(ori_lang)
# #         print(type(id))
        detailUrl = "/3/movie/"
        detailUrl += str(id)
        detailUrl += "?language=en-US&api_key=2b4a725a283b9fa435aca3507c61bae2"
          
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        conn.request("GET", detailUrl, payload)
  
        detail_res = conn.getresponse()
        detail_data = detail_res.read()
        decoded_detail = detail_data.decode("utf-8")
        json_detail = json.loads(decoded_detail)
#         print(json_detail)
# #         print(type(json_detail))
        budget = json_detail['budget']
        series_dict = json_detail['belongs_to_collection']
        if series_dict != None:
            series = 1
        else : 
            series = 0
        ori_lang_list = json_detail['spoken_languages']
#         print(ori_lang_list)
        ori_lang = []
        for one_lang in ori_lang_list:
            ori_lang.append( one_lang['iso_639_1'] )
#         print(budget) 
#         print(series)
#         print(ori_lang)
               
        creditUrl = "/3/movie/"
        creditUrl += str(id)
        creditUrl += "/credits?api_key=2b4a725a283b9fa435aca3507c61bae2"
         
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        conn.request("GET", creditUrl, payload)
         
        credit_res = conn.getresponse()
        credit_data = credit_res.read()
        decoded_credit = credit_data.decode('utf-8')
        json_detail = json.loads(decoded_credit)
#         print(json_detail)
        crew_list = json_detail['crew']
        cast_list = json_detail['cast']
#         print(crew_list)
#         print('-'*20+'crew'+'-'*20)
#         print(cast_list)
#         print('-'*20+'cast'+'-'*20)
#         print('-'*50)
    
        crewData = []
        castData = []
        for onecrew in crew_list :
            crewDict = dict()
            crewDict['name'] = onecrew['name']
            crewDict['department'] = onecrew['department']
            crewDict['gender'] = onecrew['gender']
            crewData.append(crewDict)
               
        for onecast in cast_list :
            castDict = dict()
            castDict['name'] = onecast['name']
            castDict['gender'] = onecast['gender']
            castData.append(castDict)
        
#         print(crewData)
#         print('-'*20+'crew'+'-'*20)
#         print(castData)
#         print('-'*20+'cast'+'-'*20)
 
        TMDBData.append([title, budget, ori_lang, series, crewData, castData])
#     print(movieData)
#     print('-'*50)
#     print('#'*50)

print(TMDBData)
print('finished')
    

### gender - 1: 여자 / 2: 남자 / 0 : 결측?
