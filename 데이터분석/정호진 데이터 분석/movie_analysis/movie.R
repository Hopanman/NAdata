library(tidyverse)
library(corrplot)
library(plotly)
library(ggthemes)
library(viridis)
library(gridExtra)
library(VIM)
library(lubridate)
library(randomForest)
library(lawstat)
library(varhandle)


getwd()
movie <- read.csv('movie_regression.csv', na.strings = c(''))

glimpse(movie)

movie$TITLE

movie$DIRECTOR

length(movie$TITLE)

length(movie$DIRECTOR)

movie$TITLE

movie$DIRECTOR

glimpse(movie)

table(movie$SERIES)

# movie[1:4213,] %>% group_by(DIRECTOR) %>% summarise(director_n=n()) %>% arrange(desc(director_n)) %>% filter(!is.na(DIRECTOR)) %>% head(20)

sum(movie$AUDI_ACC <= 10000)
mean(movie$AUDI_ACC)
median(movie$AUDI_ACC)



factor(movie$ORI_BOOK)
movie$ORI_BOOK <- factor(movie$ORI_BOOK)
glimpse(movie)
table(movie$ORI_BOOK)
# ggplot(movie, aes(x=ORI_BOOK, y=AUDI_ACC, fill=ORI_BOOK)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='원작도서유무에 따른 관객수 비교', x='원작도서유무', y='관객수')
ggplot(filter(movie, !is.na(ORI_BOOK)), aes(x=ORI_BOOK, y=AUDI_ACC, fill=ORI_BOOK)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(25000,50000,75000,100000), labels=c('25000명','50000명','75000명','100000명')) + scale_x_discrete(breaks=c(0,1), labels=c('없음','있음')) + theme_classic() + labs(title='원작도서유무에 따른 관객수 중앙값', x='원작도서', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')



# glimpse(movie)
# 
# sum(is.na(movie$AWARDS))
# table(movie$AWARDS)
# movie$AWARDS <- factor(movie$AWARDS)
# 
# glimpse(movie)
# 
# ggplot(movie, aes(x=AWARDS, y=AUDI_ACC, fill=AWARDS)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='수상여부에 따른 관객수 비교', x='수상여부', y='관객수')




sum(is.na(movie$SERIES))
table(movie$SERIES)
movie$SERIES <- factor(movie$SERIES)
glimpse(movie)
# ggplot(filter(movie, !is.na(SERIES)), aes(x=SERIES, y=AUDI_ACC, fill=SERIES)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='시리즈물여부에 따른 관객수 비교', x='시리즈물여부', y='관객수')
ggplot(filter(movie, !is.na(SERIES)), aes(x=SERIES, y=AUDI_ACC, fill=SERIES)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,200000,400000,600000), labels=c('0명','200000명','400000명','600000명')) + scale_x_discrete(breaks=c(0,1), labels=c('비시리즈','시리즈')) + theme_classic() + labs(title='시리즈작품여부에 따른 관객수 중앙값', x='시리즈작품여부', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




glimpse(movie)
sum(is.na(movie$WATCH_GRADE_NM))
table(movie$WATCH_GRADE_NM)
ggplot(movie, aes(x=WATCH_GRADE_NM, y=AUDI_ACC, fill=WATCH_GRADE_NM)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,10000,20000), labels=c('0명','10000명','20000명')) + theme_classic() + labs(title='관람등급에 따른 관객수 중앙값', x='관람등급', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




glimpse(movie)
sum(is.na(movie$SHOW_TM))
ggplot(movie,aes(x=SHOW_TM, y=AUDI_ACC, color=SHOW_TM)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + scale_x_continuous(breaks=c(60,120,180,240), labels=c('1시간','2시간','3시간','4시간')) + theme_classic()  + labs(title='상영시간에 따른 관객수', x='상영시간', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$SHOW_TM, movie$AUDI_ACC, use='complete.obs')






glimpse(movie)
sum(is.na(movie$BUDGET))
ggplot(filter(movie, !is.na(BUDGET)),aes(x=BUDGET, y=AUDI_ACC, color=BUDGET)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + scale_x_continuous(breaks=c(0,100000000,200000000,300000000,400000000, 500000000), labels=c('0','1억','2억','3억','4억','5억')) + theme_classic()  + labs(title='예산에 따른 관객수', x='예산(Dollar)', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$BUDGET, movie$AUDI_ACC, use='complete.obs')






glimpse(movie)
sum(is.na(movie$NAVER_CMT_NN))
ggplot(filter(movie, !is.na(NAVER_CMT_NN)),aes(x=NAVER_CMT_NN, y=AUDI_ACC, color=NAVER_CMT_NN)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000, 20000000), labels = c('0명', '오백만명', '천만명', '천오백만명', '이천만명')) + scale_x_continuous(breaks=c(0, 5000, 10000, 15000, 20000, 25000), labels=c('0건','5000건','10000건','15000건','20000건','25000건'))+ theme_classic()  + labs(title='개봉전 네이버 댓글수에 따른 관객수', x='네이버 댓글수', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_CMT_NN, movie$AUDI_ACC, use='complete.obs')





glimpse(movie)
ggplot(filter(movie, !is.na(NAVER_PRE_EVAL)),aes(x=NAVER_PRE_EVAL, y=AUDI_ACC, color=NAVER_PRE_EVAL)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + scale_x_continuous(breaks=c(0, 2.5, 5.0, 7.5, 10.0), labels=c('0점','2.5점','5점','7.5점','10점'))+ theme_classic() + labs(title='개봉전 네이버 평점에 따른 관객수', x='네이버 평점', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_PRE_EVAL, movie$AUDI_ACC, use='complete.obs')





ggplot(filter(movie, !is.na(NAVER_PRE_EVAL_MUL)),aes(x=NAVER_PRE_EVAL_MUL, y=AUDI_ACC, color=NAVER_PRE_EVAL_MUL)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000, 20000000), labels = c('0명', '오백만명', '천만명', '천오백만명','이천만명'))+ theme_classic() + labs(title='개봉전 네이버 평점x네이버 댓글수에 따른 관객수', x='네이버 평점x네이버 댓글수', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_PRE_EVAL_MUL, movie$AUDI_ACC, use='complete.obs')




glimpse(movie)
ggplot(filter(movie, !is.na(NAVER_EX_PT)),aes(x=NAVER_EX_PT, y=AUDI_ACC, color=NAVER_EX_PT)) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + theme_classic() + labs(title='개봉전 네이버 기대지수에 따른 관객수', x='기대지수', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
ggplot(filter(movie, !is.na(NAVER_EX_PT)),aes(x=log1p(NAVER_EX_PT), y=AUDI_ACC, color=log1p(NAVER_EX_PT))) + geom_point() + scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000), labels = c('0명', '오백만명', '천만명', '천오백만명')) + theme_classic() + labs(title='개봉전 네이버 기대지수(로그)에 따른 관객수', x='log(1+기대지수)', y='관객수') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')
cor(movie$NAVER_EX_PT, movie$AUDI_ACC, use='complete.obs')




ggplot(movie, aes(x=AUDI_ACC)) + geom_histogram()
geom_histogram
max(log(movie$AUDI_ACC))

glimpse(movie)

movie$OPEN_YEAR <- factor(movie$OPEN_YEAR)
movie$OPEN_MONTH <- factor(movie$OPEN_MONTH)
movie$OPEN_DAY <- factor(movie$OPEN_DAY)
movie$OPEN_WEEKDAY <- factor(movie$OPEN_WEEKDAY)
movie$OPEN_QUARTER <- factor(movie$OPEN_QUARTER)
movie$OPEN_WEEK <- factor(movie$OPEN_WEEK)



# summary(aov(AUDI_ACC~TITLE, data = movie))

# 데이터의 정규분포 여부 확인
shapiro.test(movie$AUDI_ACC)


#두 집단간 차이 분석
str(movie)
wilcox.test(AUDI_ACC~SERIES,data=movie)
glimpse(movie)
movie$AWARDS <- factor(movie$AWARDS)
wilcox.test(AUDI_ACC~AWARDS,data=movie)


#세 집단이상간 차이 분석
levene.test(movie$AUDI_ACC, movie$OPEN_YEAR, location='mean')
summary(aov(AUDI_ACC~OPEN_YEAR, data=movie))
kruskal.test(AUDI_ACC~NATION_NM_NUM, data=movie)


table(movie$ORI_BOOK)

top20_actor <- movie %>% group_by(ACTOR1) %>% summarise(actor_n = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(actor_n)) %>% filter(!is.na(ACTOR1)) %>% head(20) 


ggplot(top20_actor, aes(x=ACTOR1,y=audi_median,fill=ACTOR1)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,1000000,2000000,3000000,4000000,5000000), labels=c('0','백만명','이백만명','삼백만명','사백만명','오백만명'))  + theme_classic() + labs(title='주인공출연빈도 top20배우의 관객수 중앙값', x='배우', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none', axis.text.x = element_text(angle=90))





glimpse(movie)
top10_company <- movie %>% group_by(COMPANY_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(COMPANY_NM)) %>% head(10)
ggplot(top10_company, aes(x=COMPANY_NM,y=audi_median,fill=COMPANY_NM)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,200000,400000,600000,800000), labels=c('0','20만명','40만명','60만명','80만명'))  + theme_classic() + labs(title='빈도수 top10배급사의 관객수 중앙값', x='배급사', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()
top10_company

table(movie$PRI_GENRE_NM)
glimpse(movie)
movie %>% group_by(PRI_GENRE_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(PRI_GENRE_NM)) %>% head(20)
ggplot(filter(movie, !is.na(PRI_GENRE_NM)), aes(x=PRI_GENRE_NM, y=log(AUDI_ACC), fill=PRI_GENRE_NM)) + stat_summary_bin(fun.y = mean, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + coord_flip() + theme_classic() + labs(title='장르에 따른 관객수(로그) 평균', x='장르', y='log(관객수) 평균') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')







top20_nation <- movie %>% group_by(NATION_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(NATION_NM)) %>% head(20)
ggplot(top20_nation, aes(x=NATION_NM,y=audi_median,fill=NATION_NM)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0)  + coord_flip() + scale_y_continuous(breaks=c(0,20000,40000,60000), labels=c('0','2만명','4만명','6만명'))  + theme_classic() + labs(title='빈도수 top20제작국가의 관객수 중앙값', x='제작국가', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




table(movie$SP_LANG_NUM)
top20_lang <- movie %>% group_by(SP_LANG) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC), audi_mean=mean(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(SP_LANG)) %>% head(20)
ggplot(top20_lang, aes(x=SP_LANG,y=audi_median,fill=SP_LANG)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + coord_flip() + scale_y_continuous(breaks=c(0,200000,400000), labels=c('0','20만명','40만명')) + theme_classic() + labs(title='top20사용언어에 따른 관객수 중앙값', x='사용언어', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')

top20_lang
movie$ACTOR1

glimpse(movie)
ggplot(filter(movie, !is.na(AWARDS)), aes(x=AWARDS, y=AUDI_ACC, fill=AWARDS)) + stat_summary_bin(fun.y = median, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,10000,20000), labels=c('0','만명','2만명')) + scale_x_discrete(breaks=c(0,1), labels=c('비수상','수상')) + theme_classic() + labs(title='개봉전 수상여부에 따른 관객수 중앙값', x='수상여부', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




glimpse(movie)

train <- subset(movie, select=c(TITLE,DIRECTOR,OPEN_DT,OPEN_MONTH,	OPEN_QUARTER,OPEN_WEEK,SHOW_TM,NATION_NM,	COMPANY_NM,	PRI_GENRE_NM,	SP_LANG,	WATCH_GRADE_NM,	ACTOR1,	ACTOR2,	SERIES,	NAVER_CMT_NN,	NAVER_EX_PT,	ORI_BOOK,	AUDI_ACC))

#결측치 정보 확인
aggr(train, sortVars=T,prop=F, cex.axis=0.45, numbers=T)
aggr
glimpse(train)

table(movie$SP_LANG_NUM)
table(train$SP_LANG)

# Median VS Mean; 정규분포를 따르지 않을 때는 Median을 쓴다.
summary(train)
ggplot(train,aes(x=NAVER_EX_PT)) + geom_histogram()
ggplot(train,aes(x=NAVER_CMT_NN)) + geom_histogram()
ggplot(train,aes(x=SHOW_TM)) + geom_histogram()
shapiro.test(train$NAVER_EX_PT)
shapiro.test(train$NAVER_CMT_NN)
shapiro.test(train$SHOW_TM)




#훈련 테스트
train_omit <- na.omit(train)
glimpse(train_omit)
summary(train_omit)
train_omit <- mutate(train_omit, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1), AUDI_ACC = log10(AUDI_ACC))
#https://thebook.io/006723/ch09/02/01/03/
set.seed(222)
randomForest(AUDI_ACC ~ ., data=train_omit, ntree=501, replace=T, nodesize=9, importance=T)
rm(train_omit)




train <- subset(train, select=c(TITLE,OPEN_DT, OPEN_MONTH,OPEN_QUARTER,SHOW_TM,NATION_NM,COMPANY_NM,PRI_GENRE_NM,WATCH_GRADE_NM,SERIES,NAVER_CMT_NN,NAVER_EX_PT,ORI_BOOK,AUDI_ACC))
aggr(train,sortVars=T, prop=F, cex.axis=0.45, numbers=T)
train$SERIES[is.na(train$SERIES)] <- 0
train <- na.omit(train)

summary(train)


train$TOP_COMPANY_NM[train$COMPANY_NM=='씨제이이앤엠(주)'] <- '씨제이이앤엠(주)'
train$TOP_COMPANY_NM[train$COMPANY_NM=='롯데쇼핑㈜롯데엔터테인먼트'] <- '롯데쇼핑㈜롯데엔터테인먼트'
train$TOP_COMPANY_NM[train$COMPANY_NM=='유니버설픽쳐스인터내셔널 코리아(유)'] <- '유니버설픽쳐스인터내셔널 코리아(유)'
train$TOP_COMPANY_NM[train$COMPANY_NM=='(주)넥스트엔터테인먼트월드(NEW)'] <- '(주)넥스트엔터테인먼트월드(NEW)'
train$TOP_COMPANY_NM[train$COMPANY_NM=='(주)팝엔터테인먼트'] <- '(주)팝엔터테인먼트'
train$TOP_COMPANY_NM[train$COMPANY_NM=='(주)영화사 진진'] <- '(주)영화사 진진'
train$TOP_COMPANY_NM[train$COMPANY_NM=='이십세기폭스코리아(주)'] <- '이십세기폭스코리아(주)'
train$TOP_COMPANY_NM[train$COMPANY_NM=='워너브러더스 코리아(주)'] <- '워너브러더스 코리아(주)'
train$TOP_COMPANY_NM[train$COMPANY_NM=='와이드 릴리즈(주)'] <- '와이드 릴리즈(주)'
train$TOP_COMPANY_NM[train$COMPANY_NM=='(주)박수엔터테인먼트'] <- '(주)박수엔터테인먼트'
train$TOP_COMPANY_NM[is.na(train$TOP_COMPANY_NM)] <- '기타'

glimpse(train)
train$TOP_COMPANY_NM <- factor(train$TOP_COMPANY_NM)

train <- train[-7]

# write.csv(train, 'imsi.csv',row.names = F, fileEncoding = 'cp949')

train <- read.csv('train.csv')

train

sort(table(train$PRI_NATION_NM),decreasing = T)

glimpse(train)

train$OPEN_MONTH <- factor(train$OPEN_MONTH)
train$OPEN_QUARTER <- factor(train$OPEN_QUARTER)
train$SERIES <- factor(train$SERIES)
train$ORI_BOOK <- factor(train$ORI_BOOK)

train$NATION_NM[train$PRI_NATION_NM=='미국'] <- '미국'
train$NATION_NM[train$PRI_NATION_NM=='한국'] <- '한국'
train$NATION_NM[train$PRI_NATION_NM=='일본'] <- '일본'
train$NATION_NM[train$PRI_NATION_NM=='프랑스'] <- '프랑스'
train$NATION_NM[train$PRI_NATION_NM=='영국'] <- '영국'
train$NATION_NM[train$PRI_NATION_NM=='중국'] <- '중국'
train$NATION_NM[train$PRI_NATION_NM=='독일'] <- '독일'
train$NATION_NM[train$PRI_NATION_NM=='스페인'] <- '스페인'
train$NATION_NM[train$PRI_NATION_NM=='캐나다'] <- '캐나다'
train$NATION_NM[train$PRI_NATION_NM=='홍콩'] <- '홍콩'
train$NATION_NM[train$PRI_NATION_NM=='이탈리아'] <- '이탈리아'
train$NATION_NM[train$PRI_NATION_NM=='러시아'] <- '러시아'
train$NATION_NM[train$PRI_NATION_NM=='덴마크'] <- '덴마크'
train$NATION_NM[train$PRI_NATION_NM=='호주'] <- '호주'
train$NATION_NM[train$PRI_NATION_NM=='인도'] <- '인도'
train$NATION_NM[train$PRI_NATION_NM=='대만'] <- '대만'
train$NATION_NM[train$PRI_NATION_NM=='스웨덴'] <- '스웨덴'
train$NATION_NM[train$PRI_NATION_NM=='벨기에'] <- '벨기에'
train$NATION_NM[train$PRI_NATION_NM=='노르웨이'] <- '노르웨이'
train$NATION_NM[train$PRI_NATION_NM=='아일랜드'] <- '아일랜드'
train$NATION_NM[is.na(train$NATION_NM)] <- '기타'

train$NATION_NM <- factor(train$NATION_NM)

glimpse(train)

train <- subset(train, select = c(TITLE,OPEN_DT,OPEN_MONTH,OPEN_QUARTER,SHOW_TM,NATION_NM,TOP_COMPANY_NM,PRI_GENRE_NM,	WATCH_GRADE_NM,SERIES,NAVER_CMT_NN,NAVER_EX_PT,ORI_BOOK,AUDI_ACC))

write.csv(train,'train.csv',row.names = F, fileEncoding = 'cp949')

train <- train[-c(1,2)]

write.csv(train,'train_regression.csv',row.names = F, fileEncoding = 'cp949')
