train <- read.csv('train_regression(2).csv')
glimpse(train)


#관객수와 댓글 길이 평균과의 상관계수
cor(train$AUDI_ACC, train$NAVER_CMT_LEN_MEAN, use='complete.obs')


#댓글길이에 따른 관객수 그래프(산점도)
ggplot(train, aes(x=NAVER_CMT_LEN_MEAN, y=AUDI_ACC, color=NAVER_CMT_LEN_MEAN)) + geom_point() +  scale_color_viridis(begin = 1, end = 0, option = 'D') + geom_smooth(method = 'lm', color = 'red3', fill = 'red3') + scale_y_continuous(breaks = c(0, 5000000, 10000000, 15000000),labels = c('0', '500만명', '1000만명', '1500만명')) + theme_classic() + theme(legend.position = 'none', plot.title=element_text(hjust=0.5, face='bold')) + labs(title = '평균 네이버 댓글 길이에 따른 관객수', x = '네이버 댓글 길이', y = '관객수')



#관객수 적은 국가 정리
glimpse(train)
train$NATION_NM[train$PRI_NATION_NM=='한국'] <- '한국'
train$NATION_NM[train$PRI_NATION_NM=='미국'] <- '미국'
train$NATION_NM[train$PRI_NATION_NM=='일본'] <- '일본'
train$NATION_NM[train$PRI_NATION_NM=='영국'] <- '영국'
train$NATION_NM[train$PRI_NATION_NM=='프랑스'] <- '프랑스'
train$NATION_NM[train$PRI_NATION_NM=='벨기에'] <- '벨기에'
train$NATION_NM[train$PRI_NATION_NM=='독일'] <- '독일'
train$NATION_NM[train$PRI_NATION_NM=='아이슬란드'] <- '아이슬란드'
train$NATION_NM[train$PRI_NATION_NM=='스페인'] <- '스페인'
train$NATION_NM[train$PRI_NATION_NM=='러시아'] <- '러시아'
train$NATION_NM[train$PRI_NATION_NM=='아일랜드'] <- '아일랜드'
train$NATION_NM[train$PRI_NATION_NM=='남아프리카공화국'] <- '남아프리카공화국'
train$NATION_NM[train$PRI_NATION_NM=='중국'] <- '중국'
train$NATION_NM[train$PRI_NATION_NM=='인도'] <- '인도'
train$NATION_NM[train$PRI_NATION_NM=='핀란드'] <- '핀란드'
train$NATION_NM[train$PRI_NATION_NM=='대만'] <- '대만'
train$NATION_NM[train$PRI_NATION_NM=='홍콩'] <- '홍콩'
train$NATION_NM[train$PRI_NATION_NM=='스웨덴'] <- '스웨덴'
train$NATION_NM[train$PRI_NATION_NM=='이탈리아'] <- '이탈리아'
train$NATION_NM[train$PRI_NATION_NM=='호주'] <- '호주'
train$NATION_NM[train$PRI_NATION_NM=='덴마크'] <- '덴마크'
train$NATION_NM[train$PRI_NATION_NM=='캐나다'] <- '캐나다'
train$NATION_NM[train$PRI_NATION_NM=='아르헨티나'] <- '아르헨티나'
train$NATION_NM[is.na(train$NATION_NM)] <- '기타'
glimpse(train)
table(train$NATION_NM)
train$NATION_NM <- factor(train$NATION_NM)


