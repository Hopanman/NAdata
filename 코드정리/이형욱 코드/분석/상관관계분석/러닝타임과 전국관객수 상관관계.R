setwd('C:/Users/3731h/Desktop')

library(dplyr)

par(mfrow=c(1,1))

#파일 불러오기
testdata<-read.csv('분석용 데이터 프레임.csv',header=T)


#케이스 2
#러닝타임과 전국관객수
mydf<-subset(testdata,select = c(SHOW_TM,AUDI_ACC))

mydf

mydf<-mydf%>%filter(!is.na(SHOW_TM))

mydf

result<-cor(mydf)

#시각화
# install.packages('corrplot')
library(corrplot)

# 그래프 그려보기
corrplot(result)
corrplot(result,method='ellipse',addCoef.col='red',main='러닝타임과 전국관객수의 상관관계')

