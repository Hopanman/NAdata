library(tidyverse)
library(corrplot)
library(plotly)
library(ggthemes)
library(viridis)
library(gridExtra)
library(VIM)
library(lubridate)
library(randomForest)

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
