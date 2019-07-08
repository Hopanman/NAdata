import pandas as pd
import re

myfile='genre&sp_lang.csv'

mydf=pd.read_csv(myfile,encoding='cp949')

# print(mydf.head())


####장르 정리

GENRE_NM=mydf['GENRE_NM'].fillna('') #시리즈 타입

GENRE_NM_list=GENRE_NM.values.tolist()

# print(GENRE_NM_list[-1])

###장르 순서대로 정리하기
new_list=list()
error_list=list()
for genre in GENRE_NM_list:
    try:
        new_genre=re.sub(' ','',genre).split('/')
        new_genre=sorted(new_genre)
#     print(new_genre)
        new_list.append(new_genre)

    except Exception as e:
        print(e)
        print(genre)
        error_list.append(genre)

# print(error_list)        

# print(new_list[:10])

data_list=list()
for onegenre in new_list:
#     print(type(onegenre))
    one_word=''
    for idx in range(len(onegenre)):
        one_word=one_word+onegenre[idx]+'/'
    one_word=one_word.rstrip('/')
    data_list.append(one_word)
# print(data_list)

mydf['GENRE_NM_sorted']=data_list

# print(mydf['GENRE_NM_sorted'])


### 언어처리

SP_LANG=mydf['SP_LANG'].fillna('') #시리즈 타입

SP_LANG_list=SP_LANG.values.tolist()

# print(GENRE_NM_list[-1])

###장르 순서대로 정리하기
new_list2=list()
error_list=list()
for lang in SP_LANG_list:
    try:
        new_lang=re.sub(' ','',lang).split('/')
        new_lang=sorted(new_lang)
#     print(new_genre)
        new_list2.append(new_lang)

    except Exception as e:
        print(e)
        print(lang)
        error_list.append(lang)

# print(error_list)        

# print(new_list[:10])

data_list2=list()
for onelang in new_list2:
#     print(type(onegenre))
    one_word=''
    for idx in range(len(onelang)):
        one_word=one_word+onelang[idx]+'/'
    one_word=one_word.rstrip('/')
    data_list2.append(one_word)
# print(data_list)

mydf['SP_LANG_sorted']=data_list2

# print(mydf['SP_LANG_sorted'])

mydf.to_csv('장르 언어칼럼 수정본_190701.csv',index=None,encoding='utf-8')
print('fin')