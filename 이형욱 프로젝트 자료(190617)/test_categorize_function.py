import pandas as pd
from collections import Counter



def categorize_string_to_number(col_name):
    myfile='movie_regression.csv'
    mydf=pd.read_csv(myfile,encoding='cp949')
        
    unique_col_sorted=sorted(mydf[col_name].fillna('없음').unique().tolist())

    ###카테고리 사전 만들기 
    col_dict=dict()
    for idx,value in enumerate(unique_col_sorted):
        col_dict[value]=idx

    ###문자를 수치로 변환
    values=mydf[col_name].fillna('없음').tolist() 
    
    error_list=list()
    for idx in range(len(values)):
        try:
            values[idx]=col_dict[values[idx]]
     
        except Exception as e:
            print(e)
            error_list.append(values[idx])
    
    return values

myfile='movie_regression.csv'
mydf=pd.read_csv(myfile,encoding='cp949')
    
### 전처리 칼럼 추가
mydf['DIRECTOR2']=categorize_string_to_number('DIRECTOR')
mydf['NATION_NM2']=categorize_string_to_number('NATION_NM')
mydf['COMPANY_NM2']=categorize_string_to_number('COMPANY_NM')
mydf['GENRE_NM2']=categorize_string_to_number('GENRE_NM')
mydf['SP_LANG2']=categorize_string_to_number('SP_LANG')
mydf['WATCH_GRADE_NM2']=categorize_string_to_number('WATCH_GRADE_NM')
mydf['ACTOR1_2']=categorize_string_to_number('ACTOR1')
mydf['ACTOR2_2']=categorize_string_to_number('ACTOR2')

print(mydf.head())
