import pandas as pd
from pandas import Series
import re

myfile1='최종 네이버 영화 개봉전 댓글 및 평점.csv'
# myfile2='영진위 영화 개봉일람-영화명은 전처리된 영화명 .csv'

# df=pd.read_csv(myfile2,encoding='utf-8')
df2=pd.read_csv(myfile1,encoding='utf-8')

# kofic_title=df['영화명']
naver_title=df2['영화명']

# print(kofic_title[:10])
# print(type(kofic_title))

# kofic_title_list=kofic_title.values.flatten().tolist()
naver_title_list=naver_title.values.flatten().tolist()

# print(type(kofic_title_list))
# print(kofic_title_list[:10])

# no_use_words='[/:*?"<>|]'
no_use_word='[^a-zA-Z0-9가-힣]'
processed_title=list()

# for title in kofic_title_list:
for title in naver_title_list:
#     title=re.sub(no_use_words,'',title)
    title=re.sub(no_use_word,'',title)
    title=title.lower()
    processed_title.append(title)
# print(processed_title[:10])

##시리즈로 만들기

processed_title_=Series(data=processed_title,index=None)

df2['수정 영화명']=processed_title_

# print(df2.columns)

new_df=df2.loc[:,['영화명','수정 영화명','감독', '개봉전 평점', '총댓글수(개봉전)', '댓글모음']]
 
new_df.columns=['네이버 영화명','영화명','감독', '개봉전 평점', '총댓글수(개봉전)', '댓글모음']

# print(new_df.columns)
# print(new_df.columns)
# print(new_df.head())


new_df.to_csv('네이버 영화 일람-영화명은 전처리된 영화명 .csv',encoding='utf-8',index=None)
print('fin')
