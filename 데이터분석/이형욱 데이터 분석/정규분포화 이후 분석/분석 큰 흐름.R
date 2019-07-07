setwd('C:/Users/3731h/Desktop')

# install.packages('UsingR')
library(UsingR)
library(dplyr)

#파일 불러오기
testdata<-read.csv('movie_regression.csv',header=T)


#필요한 컬럼만 불러오기

mydf<-subset(testdata,select = c(SHOW_TM,NATION_NM_NUM,COMPANY_NM_NUM,GENRE_NM_NUM,SP_LANG_NUM,BUDGET,NAVER_CMT_NN,NAVER_EX_PT,AUDI_ACC))

mydf<-mydf%>%filter(!is.na(SHOW_TM)&!is.na(NATION_NM_NUM)&!is.na(COMPANY_NM_NUM)&!is.na(GENRE_NM_NUM)&!is.na(SP_LANG_NUM)&!is.na(BUDGET)&!is.na(NAVER_CMT_NN)&!is.na(NAVER_EX_PT)&!is.na(AUDI_ACC))

##개략적 파악
head(mydf)

summary(mydf$AUDI_ACC)

par(mfrow=c(1,1))
hist(mydf$AUDI_ACC)

  #정규분포화

#로그변환
mydf<-transform(mydf,AUDI_ACC_log=log(AUDI_ACC+1))

hist(mydf$AUDI_ACC_log,freq=T)

#제곱근변환
mydf<-transform(mydf,AUDI_ACC_sqrt=sqrt(AUDI_ACC+1))

hist(mydf$AUDI_ACC_sqrt,freq=T)

###정규성 검정
par(mfrow=c(1,3))
qqnorm(mydf$AUDI_ACC,main='Q-Q plot of AUDI_ACC')
qqline(mydf$AUDI_ACC)

qqnorm(mydf$AUDI_ACC_log,main='Q-Q plot of AUDI_ACC_log')
qqline(mydf$AUDI_ACC_log)

qqnorm(mydf$AUDI_ACC_sqrt,main='Q-Q plot of AUDI_ACC_sqrt')
qqline(mydf$AUDI_ACC_sqrt)


## 샤피로 윌크 검정(정규 분포인지 여부)
shapiro.test(mydf$AUDI_ACC)
shapiro.test(mydf$AUDI_ACC_log)
shapiro.test(mydf$AUDI_ACC_sqrt)

##t검정
#귀무가설:장르갯수와 전국관객의 평균에는 차이가 없다.

genre=mydf$GENRE_NM_NUM
audience=mydf$AUDI_ACC_log

genre
audience

  #빈도 분석을 위한 기술 통계량 구하기
table(genre,useNA = 'ifany')

  #장르 갯수와 전국관객수 교차 분할표

testtable<-table(genre,audience,useNA='ifany')

testtable

  #집단들의 비율차이 검정  

testtable

testdf<-data.frame(testtable)



#장르 갯수에 따른 전국관객수(평균)

var.test(AUDI_ACC_log ~ GENRE_NM_NUM, ttest01)

  
