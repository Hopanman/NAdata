import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series

myfile='train_regression_hwook.csv'

mydf=pd.read_csv(myfile,encoding='cp949')

# print(mydf.head())

#제작국가 더미변수를 위한 데이터 프레임 생성(NATION_NM)

col_NATION_NM=mydf['NATION_NM']

nation_unique_list=col_NATION_NM.unique().tolist()

col_NATION_NM_list=col_NATION_NM.tolist()

id_list=list() #아이디 리스트
for idx in range(len(nation_unique_list)):
    id_list.append(idx)

#'NATION_NM'에 대한 데이터프레임 생성
nation_nm_df=DataFrame({'nation_id':id_list,
                        'nation':nation_unique_list},
                        columns=['nation_id','nation'])

#####
#가변수(dummy variable) 만들기
nation_dummy_mat=pd.get_dummies(nation_nm_df['nation'])

#####
#국가별 더미 데이터 프레임 생성
indicator_mat=DataFrame(np.zeros((mydf.shape[0],len(nation_unique_list))),
                        columns=nation_unique_list)

for i,nation in enumerate(col_NATION_NM_list):
    indicator_mat.loc[i,nation]=1
# print(indicator_mat.head())
# nation_dummy_mat=nation_nm_df.join(nation_dummy_mat.add_prefix('nation_'))
imsi_mat=mydf.join(indicator_mat.add_prefix('nation_'))
# print(nation_dummy_mat)

##########################################################################
#제작회사 더미변수를 위한 데이터 프레임 생성(TOP_COMPANY_NM)

col_TOP_COMPANY_NM=mydf['TOP_COMPANY_NM']

company_unique_list=col_TOP_COMPANY_NM.unique().tolist()

col_TOP_COMPANY_NM_list=col_TOP_COMPANY_NM.tolist()

id_list=list() #아이디 리스트
for idx in range(len(company_unique_list)):
    id_list.append(idx)

#'TOP_COMPANY_NM'에 대한 데이터프레임 생성
company_nm_df=DataFrame({'company_id':id_list,
                        'company':company_unique_list},
                        columns=['company_id','company'])

#####
#가변수(dummy variable) 만들기
company_dummy_mat=pd.get_dummies(company_nm_df['company'])

#####
#국가별 더미 데이터 프레임 생성
indicator_mat=DataFrame(np.zeros((mydf.shape[0],len(company_unique_list))),
                        columns=company_unique_list)

for i,company in enumerate(col_TOP_COMPANY_NM_list):
    indicator_mat.loc[i,company]=1
# print(indicator_mat.head())
# nation_dummy_mat=nation_nm_df.join(nation_dummy_mat.add_prefix('nation_'))
nation_company_mat=imsi_mat.join(indicator_mat.add_prefix('company_'))
print(nation_company_mat)


nation_company_mat.to_csv('시험용 더미 데이터프레임.csv',index=None,encoding='cp949')
print('완료')

# print(mydf.shape)