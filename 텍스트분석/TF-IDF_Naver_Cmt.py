import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import numpy as np

movie = pd.read_csv('D:/myworkspace/github/movie_text.csv')
pd.set_option('max_column',None)

vectorizer = TfidfVectorizer(
                sublinear_tf=True,
                analyzer='word',
                token_pattern=r'\w{1,}',
    )

overview_text = vectorizer.fit_transform(movie['NAVER_CMT'].fillna(''))


word2id = defaultdict(lambda : 0)

for idx, feature in enumerate(vectorizer.get_feature_names()):
    word2id[feature] = idx
   
   
for i, sent in enumerate(movie['NAVER_CMT'].fillna('').str.replace('[\W]+', ' ')):
    if i >=3:
        break
#     print(i, sent)
#     print(sent.split())
#     print('-'*50)
    print('====== document[%d] ======' % i)
    mylist = [ (token, overview_text[i, word2id[token]]) for token in sent.split() ]
    mylist = list( set(mylist) )
    sorted_by_value = sorted(mylist, key=lambda tup : tup[1], reverse = True)
    print(sorted_by_value[0:10])
    
    print('-'*50)
    


# for col in movie['PLOT'].fillna('').str.replace('[\W]+', ' '):
#     print(col)
#     print('-'*50)
#     break
    
