import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series

myfile='시험용 더미 데이터프레임2.csv'

mydf=pd.read_csv(myfile,encoding='cp949')

def onehotencoding(colname):
    
    #해당컬럼(제작국가) 더미변수를 위한 데이터 프레임 생성(NATION_NM)
    
    column=mydf[str(colname)]
    
    column_unique_list=column.unique().tolist()
    
    col_total_list=column.tolist()
    
    id_list=list() #아이디 리스트
    for idx in range(len(column_unique_list)):
        id_list.append(idx)
    
    #해당컬럼('NATION_NM')에 대한 데이터프레임 생성
    column_df=DataFrame({(str(colname)+'_id'):id_list,
                            str(colname):column_unique_list},
                            columns=[(str(colname)+'_id'),(str(colname))])
    
    #####
    #가변수(dummy variable) 만들기
    column_dummy_mat=pd.get_dummies(column_df[str(colname)])
    
    #####
    #국가별 더미 데이터 프레임 생성
    indicator_mat=DataFrame(np.zeros((mydf.shape[0],len(column_unique_list))),
                            columns=column_unique_list)
    
    for i,content in enumerate(col_total_list):
        indicator_mat.loc[i,content]=1
    # print(indicator_mat.head())
    # nation_dummy_mat=nation_nm_df.join(nation_dummy_mat.add_prefix('nation_'))
    
    imsi_mat=mydf.join(indicator_mat.add_prefix(str(colname)+'_'))
    
    return imsi_mat

onehotencoding('WATCH_GRADE_NM').to_csv('시험용 더미 데이터프레임3.csv',index=None,encoding='cp949')
print('fin')    