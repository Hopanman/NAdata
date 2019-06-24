import pandas as pd

file1='네이버 영화 일람-영화명은 전처리된 영화명 .csv'
# file1='최종 네이버 영화 개봉전 댓글 및 평점.csv'
# file2='영진위 영화 개봉일람(2010~2019).csv'
# file2='영진위 영화 개봉일람-영화명은 전처리된 영화명 .csv'
file2='영진위 영화 개봉일람-영화명은 전처리된 영화명 2.csv'

naver_df=pd.read_csv(file1,encoding='utf-8')
kofic_df=pd.read_csv(file2,encoding='utf-8')

kofic_df2=kofic_df.loc[kofic_df['전국관객수']!='1',:]
kofic_df2=kofic_df2.loc[kofic_df['전국관객수']!='0',:]

imsi_df=pd.merge(naver_df,kofic_df2,on=['영화명','감독'],how='inner')
imsi_df2=pd.merge(naver_df,kofic_df2,on=['영화명','감독'],how='outer',indicator=True)


imsi_df3=imsi_df2.loc[imsi_df2['_merge']!='both']

# print(imsi_df.shape)    #5087, 21

# print(imsi_df2.columns)
# print(imsi_df2.shape)    #15348,22

# print(imsi_df3.shape)    #10262, 22

# imsi=kofic_df['전국관객수'].values.flatten().tolist()
# print(type(kofic_df['전국관객수'].values.flatten().tolist()))
# print(type(imsi[0]))
# print(imsi[0])

# print(kofic_df.shape) #10465,19
# print(kofic_df2.shape) #7676


imsi_df.to_csv('영진위 네이버와 겹치는 영화3 .csv',encoding='utf-8',index=None)
imsi_df3.to_csv('영진위 네이버 겹치지 않는 영화3.csv',encoding='utf-8',index=None)
print('최종 데이터 프레임.csv 저장 완료')

print('fin')