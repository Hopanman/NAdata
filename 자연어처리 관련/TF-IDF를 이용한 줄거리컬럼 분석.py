import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import numpy as np

movie = pd.read_csv('NAdata/movie.csv')
pd.set_option('max_column',None)

vectorizer = TfidfVectorizer(
                sublinear_tf=True,
                analyzer='word',
                token_pattern=r'\w{1,}',
    )

overview_text = vectorizer.fit_transform(movie['PLOT'].fillna(''))

word2id = defaultdict(lambda : 0)

for idx, feature in enumerate(vectorizer.get_feature_names()):
    word2id[feature] = idx


for i, sent in enumerate(list(movie['PLOT'].fillna(''))):
    if i >=1:
        break
    print('====== document[%d] ======' % i)
    print( [ (token, overview_text[i, word2id[token]]) for token in sent.split() ])

