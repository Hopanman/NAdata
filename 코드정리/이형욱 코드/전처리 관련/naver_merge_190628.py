import pandas as pd

file1='네이버크롤링 추가작업 _190628.csv'
file2='네이버&영진위겹치는영화(최종_호진).csv'

hwook_df=pd.read_csv(file1,encoding='utf-8')
hojin_df=pd.read_csv(file2,encoding='cp949')

imsi_df=pd.merge(hwook_df,hojin_df,on=['영화명','감독'],how='inner')
imsi_df2=pd.merge(hwook_df,hojin_df,on=['영화명','감독'],how='outer',indicator=True)
imsi_df3=imsi_df2.loc[imsi_df2['_merge']!='both']

# print(imsi_df.columns)

imsi_df4=imsi_df.drop(['원작도서유무'],axis=1)
imsi_df4=imsi_df.drop(['네이버기대지수'],axis=1)

# print(len(imsi_df4.columns))
# print(hwook_df.shape)
# print(hojin_df.shape)
# print(imsi_df.shape)
# print(imsi_df3.loc[imsi_df3['_merge']=='left_only'])

# imsi_df4.to_csv('네이버크롤링 추가작업 _190628(머지버전).csv',index=None,encoding='utf-8')
# print('csv 저장 완료.')

file3='감독명 수정  네이버 덧글 영진위 자료_190628.csv'
file4='네이버크롤링 추가작업 _190628(머지버전).csv'
# 
df_before=pd.read_csv(file3,encoding='utf-8')
df_add=pd.read_csv(file4,encoding='utf-8')
# 
# print(len(df_before.columns))
final_df=pd.concat([df_before,df_add])

# final_df.to_csv('네이버 (개봉전) 영진위 최종 (형욱).csv',index=None,encoding='utf-8')
# print('csv 저장 완료.')

# print(final_df.shape)
# print(final_df.columns)

imsi_df5=pd.merge(final_df,hojin_df,on=['영화명','감독'],how='outer',indicator=True)
imsi_df6=imsi_df5.loc[imsi_df5['_merge']!='both']

print(imsi_df6.loc[imsi_df6['_merge']=='right_only',['영화명','감독']])
