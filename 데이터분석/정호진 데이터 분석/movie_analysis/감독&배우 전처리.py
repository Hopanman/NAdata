
# coding: utf-8

# In[1]:

import pandas as pd


# In[3]:

movie = pd.read_csv('NAdata/movie_regression.csv',encoding='cp949')


# In[5]:

train = pd.read_csv('NAdata/train(2차).csv',encoding='cp949')


# In[7]:

pd.set_option('max_column',None)


# In[8]:

movie


# In[10]:

movie = movie.loc[:,['TITLE','DIRECTOR','OPEN_DT','ACTOR1']]


# In[11]:

movie.head(1)


# In[12]:

movie.loc[:,'OPEN_DT'] = pd.to_datetime(movie['OPEN_DT'])


# In[13]:

movie.info()


# In[14]:

train.head(1)


# In[15]:

train.loc[:,'OPEN_DT'] = pd.to_datetime(train['OPEN_DT'])


# In[16]:

train.info()


# In[18]:

train = pd.merge(train,movie,'inner',['TITLE','OPEN_DT'])


# In[20]:

train.columns


# In[23]:

train = train.reindex(columns=['TITLE', 'DIRECTOR', 'OPEN_DT', 'OPEN_MONTH', 'OPEN_QUARTER', 'OPEN_WEEK',
       'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM','ACTOR1',
       'SERIES', 'NAVER_CMT_NN', 'NAVER_CMT_LEN_MEAN', 'NAVER_EX_PT',
       'ORI_BOOK', 'AUDI_ACC'])


# In[25]:

train.to_csv('train(3차임시).csv',index=False,encoding='cp949')


# In[66]:

train = pd.read_csv('train(3차임시).csv',encoding='cp949')


# In[67]:

train


# In[103]:

pd.set_option('max_row',60)


# In[73]:

4.014770e+05


# In[76]:

director = train.groupby('DIRECTOR')['AUDI_ACC'].mean().sort_values(ascending=False)


# In[79]:

director = director[director >= 400000]


# In[82]:

director.index


# In[84]:

for i in director.index:
    train.loc[train['DIRECTOR'] == i,'TOP_DIRECTOR'] = i


# In[87]:

train


# In[88]:

train.loc[train['TOP_DIRECTOR'].isna(),'TOP_DIRECTOR'] = '기타'


# In[89]:

len(train['TOP_DIRECTOR'].value_counts())


# In[90]:

train


# In[95]:

1.006075e+06


# In[96]:

actor = train.groupby('ACTOR1')['AUDI_ACC'].mean().sort_values(ascending=False)


# In[99]:

actor = actor[actor >= 1000000]


# In[100]:

actor.index


# In[101]:

for i in actor.index:
    train.loc[train['ACTOR1'] == i,'TOP_ACTOR'] = i


# In[104]:

train


# In[105]:

train.loc[train['TOP_ACTOR'].isna(),'TOP_ACTOR'] = '기타'


# In[107]:

len(train['TOP_ACTOR'].value_counts())


# In[108]:

train


# In[109]:

train.info()


# In[110]:

train.head(1)


# In[111]:

train.columns


# In[112]:

train = train.loc[:,['OPEN_MONTH', 'OPEN_QUARTER','OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM',
       'WATCH_GRADE_NM','SERIES', 'NAVER_CMT_NN','NAVER_EX_PT', 'ORI_BOOK', 'AUDI_ACC','TOP_DIRECTOR', 'TOP_ACTOR']]


# In[114]:

train


# In[113]:

train.columns


# In[115]:

train = train.reindex(columns=['TOP_DIRECTOR','OPEN_MONTH', 'OPEN_QUARTER', 'OPEN_WEEK', 'SHOW_TM', 'NATION_NM',
       'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM','TOP_ACTOR', 'SERIES',
       'NAVER_CMT_NN', 'NAVER_EX_PT', 'ORI_BOOK', 'AUDI_ACC'])


# In[116]:

train


# In[117]:

train.to_csv('train_regression(최종).csv',index=False,encoding='cp949')


# In[ ]:



