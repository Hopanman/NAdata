library(MASS) 
library(randomForest) 
library(caret)

newdata <- read.csv('C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/cmtScore_alldata.csv')
tail(newdata)
names(newdata)
summary(newdata)
str(newdata)

newdata$SERIES[is.na(newdata$SERIES)] <- 0
newdata$OPEN_WEEK <- as.factor(newdata$OPEN_WEEK)
newdata$SERIES <- as.factor(newdata$SERIES)

newdata['AUDI_ACC'] <- log( newdata['AUDI_ACC'] )
newdata['NAVER_CMT_NN'] <- log( newdata['NAVER_CMT_NN'] )
newdata['NAVER_EX_PT'] <- log( newdata['NAVER_EX_PT'] )
# newdata['OPEN_WEEK'] <- log( newdata['OPEN_WEEK'] )
# newdata['SHOW_TM'] <- log( newdata['SHOW_TM'] )

newdata$AUDI_ACC[is.infinite(newdata$AUDI_ACC)] <- 0
newdata$NAVER_CMT_NN[is.infinite(newdata$NAVER_CMT_NN)] <- 0
newdata$NAVER_EX_PT[is.infinite(newdata$NAVER_EX_PT)] <- 0
# newdata$OPEN_WEEK[is.infinite(newdata$OPEN_WEEK)] <- 0
# newdata$SHOW_TM[is.infinite(newdata$v)] <- 0

set.seed(10)


fitdata = newdata[c('OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM', 'SERIES', 'NAVER_CMT_NN', 'NAVER_EX_PT', 'CMT_SCORE', 'AUDI_ACC')]

dim(fitdata)

fitdata <- na.omit(fitdata)

dim(fitdata)

names(fitdata)

# rfcr.fit <- train(AUDI_ACC~., data=fitdata, method='rf')
rfcr.fit <- train(AUDI_ACC~., data=fitdata, method='ranger')



test_x <- fitdata[c('OPEN_WEEK', 'SHOW_TM', 'NATION_NM', 'COMPANY_NM', 'PRI_GENRE_NM', 'WATCH_GRADE_NM', 'SERIES', 'NAVER_CMT_NN', 'NAVER_EX_PT', 'CMT_SCORE', 'AUDI_ACC')]

test_y = fitdata$AUDI_ACC

y_pred = predict(rfcr.fit, test_x)

cbind(exp(test_y), exp(y_pred))
cbind(test_y, y_pred)

head( fitdata )

result <- cbind(fitdata, y_pred, exp(test_y), exp(y_pred)) 

write.csv(result, 'C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/caretResult_addCmtscore.csv', row.names=F, quote=F, fileEncoding='UTF-8')

summary(rfcr.fit)

capture.output(rfcr.fit, file = 'C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/rfcr_addCmtscore.fit.txt', append=TRUE)

capture.output(summary(rfcr.fit), file = 'C:/Users/user/Documents/github/영화 예측 관련/caretResult_김지수/summary_rfcr.fit_addCmtscore.txt', append=TRUE)