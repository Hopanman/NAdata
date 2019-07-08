data <- read.csv('C:/myworkspace/pydevProject/polarityDict/cmtScore_audiAcc.csv')

head(data)
str(data)
dim(data)

data <- na.omit(data)

data$AUDI_ACC <- as.numeric(data$AUDI_ACC)

# help(cor)

######### CMT_SCORE - AUDI_ACC 惑包包拌

plot(data$CMT_SCORE, data$AUDI_ACC)
plot(data$CMT_SCORE, log(data$AUDI_ACC))
plot(data$CMT_SCORE, sqrt(data$AUDI_ACC))

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


######### CMT_SCORE - NAVER_PRE_EVAL 惑包包拌

plot(data$CMT_SCORE, data$NAVER_PRE_EVAL)

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

