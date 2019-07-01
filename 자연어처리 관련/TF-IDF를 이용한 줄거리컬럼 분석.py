#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import numpy as np


# In[3]:


movie = pd.read_csv('NAdata/movie.csv')


# In[6]:


pd.set_option('max_column',None)


# In[7]:


movie


# In[13]:


movie['PLOT'][0]


# In[17]:


vectorizer = TfidfVectorizer(
                sublinear_tf=True,
                analyzer='word',
                token_pattern=r'\w{1,}',
    )


# In[20]:


overview_text = vectorizer.fit_transform(movie['PLOT'].fillna(''))


# In[21]:


overview_text


# In[32]:


word2id = defaultdict(lambda : 0)


# In[34]:


for idx, feature in enumerate(vectorizer.get_feature_names()):
    word2id[feature] = idx


# In[46]:


for i, sent in enumerate(list(movie['PLOT'].fillna(''))):
    if i >=1:
        break
    print('====== document[%d] ======' % i)
    print( [ (token, overview_text[i, word2id[token]]) for token in sent.split() ])


# In[47]:


overview_text.shape

