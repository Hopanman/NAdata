from NaverMovieFinal.Step1_class_NaverAPI2 import GetMovieJson
from NaverMovieFinal.Step1_class_NaverAPI2 import GetMovieList
from NaverMovieFinal.Step1_class_NaverAPI2 import Get_Oribook_Expt
import pandas as pd 

movieJson = GetMovieJson()
movieList = GetMovieList()
OribookExpt = Get_Oribook_Expt()

result = OribookExpt.getOribookExpt('KOFIC_data(2010-2019).csv')
print(result)

print('finished')



