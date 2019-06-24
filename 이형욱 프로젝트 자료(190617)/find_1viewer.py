import pandas as pd

myfile='영진위 영화 개봉일람(2010~2019).csv'

kofic_df=pd.read_csv(myfile,encoding='utf-8')

# print(kofic_df.head())

viewer1=kofic_df.loc[kofic_df['전국관객수']=='1',['영화명']]
# print(viewer1)

viewer1_list=viewer1.values.flatten().tolist()
# print(viewer1_list)
# print(len(viewer1_list))

###########################
file1='(누락 영화-연도차이 ,무삭제판 제외)중 감독판 목록 .csv'
ommitted_json_df=pd.read_csv(file1,encoding='cp949')

ommitted_json_list=ommitted_json_df.values.flatten().tolist()

# print(ommitted_json_df.head())
# print(len(ommitted_json_list))


########################3
for title in viewer1_list:
    if title in ommitted_json_list:
        ommitted_json_list.remove(title)
# print(len(ommitted_json_list))

newdf=pd.DataFrame()
for atitle in ommitted_json_list:
    onemovie=kofic_df.loc[kofic_df['영화명']==atitle,['영화명','개봉일']]
    newdf=pd.concat([newdf,onemovie])

# print(newdf.head())

newdf.to_csv('(누락 영화-연도차이 ,무삭제판 제외,전국관객수==1제외)중 감독판 목록 .csv',encoding='cp949',index=False)
print('(누락 영화-연도차이 ,무삭제판 제외,전국관객수==1제외)중 감독판 목록 .csv 저장완료')



print('fin')