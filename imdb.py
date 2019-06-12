
import pandas as pd
fn = 'C:/Users/3731h/Documents/GitHub/project/IMDB 데이터셋/title.basics.tsv'
content=pd.read_csv(fn,delimiter='\t')
# print(content.head())
# print(content.columns)

# print(mylist)

# print(content[['titleId']])

###movie basic
aladdin=(content.loc[content['primaryTitle']=='Aladdin'])
result=aladdin.loc[aladdin['startYear']=='2019'] #연도는 문자열 처리해야함
# print(result)

###crew
fn = 'C:/Users/3731h/Documents/GitHub/project/IMDB 데이터셋/title.crew.tsv'
content=pd.read_csv(fn,delimiter='\t')

crew_aladdin=(content.loc[content['tconst']=='tt6139732'])
# print(crew_aladdin)

crew_list=['nm0005363','nm0041864','nm0005363']

fn = 'C:/Users/3731h/Documents/GitHub/project/IMDB 데이터셋/name.basics.tsv'
content=pd.read_csv(fn,delimiter='\t')

result_list=list()
for num in crew_list:
    name_crew_aladdin=(content.loc[content['nconst']==num])
    result_list.append(name_crew_aladdin)
# print(result_list)

###pricpal cast/crew

fn ='C:/Users/3731h/Documents/GitHub/project/IMDB 데이터셋/title.principals.tsv'
content=pd.read_csv(fn,delimiter='\t')

cast_aladdin=(content.loc[content['tconst']=='tt6139732'])
print(cast_aladdin)