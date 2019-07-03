setwd('C:/Users/3731h/Desktop')

library(dplyr)

par(mfrow=c(1,1))

#파일 불러오기
testdata<-read.csv('분석용 데이터 프레임.csv',header=T)

#명목형 데이터 불러오기
mydf<-subset(testdata,select = c(DIRECTOR,NATION_NM,COMPANY_NM,GENRE_NM,SP_LANG,SERIES,AWARDS,ORI_BOOK))

mydf


#결측치 처리
mydf<-mydf%>%filter(!is.na(DIRECTOR) & !is.na(NATION_NM)& !is.na(COMPANY_NM)& !is.na(GENRE_NM)& !is.na(SP_LANG)& !is.na(SERIES)& !is.na(AWARDS)& !is.na(ORI_BOOK))

mydf$SERIES<-as.factor(mydf$SERIES)
mydf$AWARDS<-as.factor(mydf$AWARDS)
mydf$ORI_BOOK<-as.factor(mydf$ORI_BOOK)

# a<-summary(mydf)
# 
# a

tablea<-table(mydf$DIRECTOR)

tablea<-(tablea)

tablea<-sort(tablea,decreasing = T)

tablea<-tablea[10,]

mode(tablea)

barplot(tablea)

#시각화

