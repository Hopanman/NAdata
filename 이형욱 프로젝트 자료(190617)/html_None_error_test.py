import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from itertools import count

myfile='링크모음.csv'

mylink=pd.read_csv(myfile)

# print(mylink)

result=mylink.values
onelist=result.tolist()
link=onelist[0][1] #onelist[idx][1]

# print(onelist[:3])
# print(link)

# print(type(result))
# print(len(result))

#하나의 링크와 그링크 하나의 덧글페이지로 테스트
onelink='https://movie.naver.com/movie/bi/mi/basic.nhn?code=159569'
onelink=onelink.replace('basic','point')
# onelink+='&type=before&page=1' #1페이지 한해서만 가지고오는것이므로 페이지에 대하여 정의필요
resp=requests.get(onelink)
html=BeautifulSoup(resp.content,'html.parser')
# print(onelink)
# print(html)

#전체 평점 
beforePoinArea=html.find(id='beforePointArea')
# print(beforePoinArea)

starscore=beforePoinArea.find('div',{'class':'star_score'})
scorelist=starscore.findAll('em')
score=''
for oneitem in scorelist:
    number1=oneitem.getText()
    score+=number1
# print(score)


##덧글 및 평점
score_result=html.find('div',{'class':'score_result'})
print(score_result)
# lis=score_result.findAll('li')
# print(lis[0])
# print(score_result)

#댓글 내용
# reply=lis[0].find('p').getText()
# print(reply)

#개인평점
# score=lis[0].find('em').getText()
# print(score)

##전체댓글수
# score_total=html.find('div',{'class':'score_total'})
# ems=score_total.findAll('em')
# total_reply=ems[1].getText()
# print(total_reply)

