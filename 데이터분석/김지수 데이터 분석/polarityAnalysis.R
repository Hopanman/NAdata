data <- read.csv('C:/myworkspace/pydevProject/polarityDict/cmtScore_audiAcc.csv')

head(data)
str(data)
dim(data)

data <- na.omit(data)

data$AUDI_ACC <- as.numeric(data$AUDI_ACC)

# help(cor)

######### CMT_SCORE - AUDI_ACC 상관관계


cordata <- subset(data, select=c(CMT_SCORE, AUDI_ACC))

pearson <- cor(cordata, method='pearson')
kendall <- cor(cordata, method='kendall')
spearman <- cor(cordata, method='spearman')

# help(corrplot)

install.packages('corrplot')
library(corrplot)

corrplot(pearson, method='ellipse', addCoef.col='red')

corrplot(kendall, method='ellipse', addCoef.col='red')

corrplot(spearman, method='ellipse', addCoef.col='red')


######### CMT_SCORE - NAVER_PRE_EVAL 상관관계

cordata <- subset(data, select=c(CMT_SCORE, NAVER_PRE_EVAL))

pearson <- cor(cordata, method='pearson')
kendall <- cor(cordata, method='kendall')
spearman <- cor(cordata, method='spearman')

# help(corrplot)

# install.packages('corrplot')
# library(corrplot)

corrplot(pearson, method='ellipse', addCoef.col='red')

corrplot(kendall, method='ellipse', addCoef.col='red')

corrplot(spearman, method='ellipse', addCoef.col='red')



ggplot(chartdata , aes( x=X1, y=log(X2), fill=X1 )) + geom_point(color='navy', shape=21, size=2, stroke=0) + labs(x='감성 점수', y='누적 관객수', title='감성 점수별 누적 관객수', fill='감성 점수') + scale_fill_viridis(begin = 1, end = 0, option = 'D') + theme_classic() + theme(legend.position = 'none') + geom_smooth(method='auto', color='red3') + scale_x_continuous(breaks=c(-1, -0.5, 0, 0.5, 1), labels=c('-1점','-0.5점', '0점', '0.5점','1점')) + scale_y_continuous(breaks = c(0, log(5000000), log(10000000), log(15000000) ), labels = c('', '오백만명', '천만명', '천오백만명'))