movie <- read.csv('train_regression(2차).csv', na.strings = c(''))

glimpse(movie)

top10_company <- movie %>% group_by(COMPANY_NM) %>% summarise(cnt = n(), audi_median=median(AUDI_ACC)) %>% arrange(desc(cnt)) %>% filter(!is.na(COMPANY_NM)&!(COMPANY_NM=='기타')) %>% head(10)
ggplot(top10_company, aes(x=reorder(COMPANY_NM,audi_median),y=audi_median,fill=COMPANY_NM)) + geom_bar(stat='identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,500000,1000000,1500000), labels=c('0','50만명','100만명','150만명'))  + theme_classic() + labs(title='빈도수 top10배급사의 관객수 중앙값', x='배급사', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()


ggplot(filter(movie, !is.na(PRI_GENRE_NM)), aes(x=PRI_GENRE_NM, y=log(AUDI_ACC), fill=PRI_GENRE_NM)) + stat_summary_bin(fun.y = mean, geom='bar') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + coord_flip() + theme_classic() + labs(title='장르에 따른 관객수(로그) 평균', x='장르', y='log(관객수) 평균') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none')




# glimpse(movie)
# top10_actor <- movie %>% group_by(ACTOR1) %>% summarise(cnt = n(), audi_sum=sum(AUDI_ACC)) %>% arrange(desc(audi_sum)) %>% filter(!is.na(ACTOR1)) %>% head(10)
# 
# ggplot(top10_actor, aes(x=ACTOR1, y=audi_sum, fill=ACTOR1)) + geom_bar(stat = 'identity') + scale_fill_viridis(discrete = T, option = 'E', begin = 1, end = 0) + scale_y_continuous(breaks=c(0,200000,400000,600000,800000), labels=c('0','20만명','40만명','60만명','80만명'))  + theme_classic() + labs(title='빈도수 top10배급사의 관객수 중앙값', x='배급사', y='관객수 중앙값') + theme(plot.title=element_text(hjust=0.5, face='bold'), legend.position = 'none') + coord_flip()



movie %>% group_by(DIRECTOR) %>% summarise(cnt = n(), audi_sum=sum(AUDI_ACC)) %>% arrange(desc(audi_sum)) %>% filter(!is.na(DIRECTOR)) %>% head(10)