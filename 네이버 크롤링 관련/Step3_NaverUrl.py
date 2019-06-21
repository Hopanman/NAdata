from naver_Oribook_Expt.Step2_Naver_API_MovieDict import runClassNaverAPI
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re


class getBookExpt:
    def getOribook_expt(self, filename):
        self.filename = filename

        getMovieList = runClassNaverAPI()
        
        movieList = getMovieList.getKoficData(self.filename)
        # print(movieList)
        
        oribook_expt = []
    
        for oneList in movieList:
            koficNm = oneList[0]
            koficDr = oneList[1]
            naverResult = oneList[2]
            if naverResult != None:
                naverDictList = naverResult['items']
                for naverDict in naverDictList:
                    movieNm = naverDict['title'].replace('<b>','').replace('</b>','')
                    movieEnNm = naverDict['subtitle']
                    openYr = naverDict['pubDate']
                    movieDr = naverDict['director'].replace('<b>','').replace('</b>','')
                    movieDr = movieDr.rstrip('|').split('|')
                          
                    if movieNm == koficNm:
                        if movieDr == koficDr:
                            naverUrl = naverDict['link']   
                                           
                            response = urlopen(naverUrl)
                                       
                            soup = BeautifulSoup(response, 'html.parser')
                        #     print(soup)
                                             
                            ###### 원작 도서 시작 
                            # 원작도서 있음 : 1 / 없음 : 0
                            myLi = soup.find('a', attrs={'title':'원작 도서'})
                            if myLi != None:
                                ori_book = 1
                            else:
                                ori_book = 0
                            print('원작도서 : %d' % (ori_book))
                            ###### 원작 도서 끝
                                              
                            ###### 기대지수 시작
                            naver_ex_pt = soup.select_one('span#interest_cnt_basic')
                            if naver_ex_pt != None:
                                naver_ex_pt = naver_ex_pt.get_text()
                                naver_ex_pt = re.sub('[가-히]+','', naver_ex_pt)
                                naver_ex_pt = naver_ex_pt.replace(',', '')
                                naver_ex_pt = int(naver_ex_pt)
                                print('기대지수 : %s' % (naver_ex_pt))
                                ###### 기대지수 끝
                            else :
                                naver_ex_pt = ''
                            oribook_expt.append([movieNm, movieEnNm, openYr, movieDr, ori_book, naver_ex_pt])
                            print('-'*50)  
                                 
                        else:
                            print('감독 다름') 
                            print([koficNm, movieNm, koficDr, movieDr])
                            pass
                        ############# ** 해외 감독의 경우 한글표기가 다르게 되어서 안 나오는 경우 있음 (아이언맨3 : 셰인 블랙 / 쉐인 블랙)
                        ############# 나중에 영진위에서 영화 영문 제목 가져와서 비교해도 괜찮을 것 같음
                            # if movieDr[0][0:2] == koficDr[0][0:2]:
                                # naverUrl = naverDict['link'] 
                                # print([koficNm, movieNm, koficDr, movieDr, naverUrl])  
                            # elif movieDr[0][-2:] == koficDr[0][-2:]:
                                # naverUrl = naverDict['link'] 
                                # print([koficNm, movieNm, koficDr, movieDr, naverUrl])
                            # else :
                                # print('감독 다름') 
                                # print([koficNm, movieNm, koficDr, movieDr])
                                # pass
                        ############## ** 검색결과가 많이 나오는 경우 해당 영화가 아예 안나오기도 함.(아바타 : 제임스 카메론 => 다른 영화만 나옴) 
                        ############## 링크를 10000부터 숫자로 하는 것도 고려해봐야할 듯.           
                    else :
                        print('제목 다름')
                        print([koficNm, movieNm, koficDr, movieDr])
                        pass 
                    print('-'*50)
                
            else :
                movieNm = ''
                movieEnNm = ''
                openYr = ''
                movieDr = ''
            print(koficNm)
            print(koficDr)
            # print(naverDictList)
            print('#'*50)
            
        print(oribook_expt)
        return oribook_expt
        
            


# print(UrlList)


getNaverData = getBookExpt()

NaverData = getNaverData.getOribook_expt('KOFIC_data(2010-2019).csv')
                
NaverDf = pd.DataFrame(NaverData, columns=['movieNm', 'movieEnNm', 'openYr', 'movieDr', 'ori_book', 'naver_ex_pt'])
print('@'*50)
print(NaverDf)

# NaverDf.to_csv('naver_Oribook_Expt(1).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(2).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(3).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(4).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(5).csv', header=True, index = False, encoding='utf-8')
# NaverDf.to_csv('naver_Oribook_Expt(6).csv', header=True, index = False, encoding='utf-8')
NaverDf.to_csv('naver_Oribook_Expt(2)_second.csv', header=True, index = False, encoding='utf-8')


print('finished')   
   
   
   
   
