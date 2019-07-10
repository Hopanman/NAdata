import pandas as pd 
import nltk
from konlpy.tag import Okt
from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag._komoran import Komoran

data = pd.read_csv('C:/Users/user/Documents/github/movie.csv')

# data = data.iloc[0:2, :]

# print(data.columns)
    
text = ' '.join([str(oneCmt) for oneCmt in data['NAVER_CMT']])
   
stop_words = ['은', '는', '이', '가', '을', '를', '에', '의', '과', '와', '둘', '등']
 
def get_tags(text, ntags):
    try : 
        spliter = Okt()
        nouns = spliter.nouns(text)
#         komoran = Komoran()
#         nouns = komoran.nouns(text)
        nouns = [each_word for each_word in nouns if each_word not in stop_words ]
#         print(nouns[0])
        nouns = nltk.Text(nouns)
        wcData = nouns.vocab().most_common(ntags)
        wcDict = dict(wcData)
        return wcDict
    except :
        pass
  
  
wcInput = get_tags(text, 100)
  
# jpype._jexception.OutOfMemoryErrorPyRaisable: java.lang.OutOfMemoryError: Java heap space
# jpype._jexception.NullPointerExceptionPyRaisable: java.lang.NullPointerException
  
print(wcInput)
print(sorted(wcInput.items(), key=lambda x:x[1], reverse=True))
        
wordcloud = WordCloud(font_path='c:/Windows/fonts/malgun.ttf', 
                      relative_scaling=0.2, 
                      background_color='black').generate_from_frequencies(wcInput)
                                 
plt.figure(figsize=(30, 50))                    
plt.imshow(wordcloud)
plt.title('Top keyword')
plt.axis('off')
plt.show()
plt.savefig('C:/myworkspace/pydevProject/sentimentAnalysis/cmtWordcloud.png', dpi=400, bbox_inches='tight')
         
print('finished')