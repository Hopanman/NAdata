setwd('C:/Users/3731h/Desktop')

library(dplyr)

par(mfrow=c(1,1))

#파일 불러오기
testdata<-read.csv('movie_regression.csv',header=T)
testdata<-transform(testdata,AUDI_ACC_log=log(AUDI_ACC+1))

#
mydf<-subset(testdata,select = c(NATION_NM_NUM,COMPANY_NM_NUM,GENRE_NM_NUM,SP_LANG_NUM,AUDI_ACC))

head(mydf)

mydf<-mydf%>%filter(!is.na(NATION_NM_NUM) & !is.na(COMPANY_NM_NUM)& !is.na(GENRE_NM_NUM)& !is.na(SP_LANG_NUM)& !is.na(AUDI_ACC))

mydf

result<-cor(mydf)

#시각화
# install.packages('corrplot')
library(corrplot)

# 그래프 그려보기
corrplot(result)
corrplot(result,method='ellipse',addCoef.col='red')

