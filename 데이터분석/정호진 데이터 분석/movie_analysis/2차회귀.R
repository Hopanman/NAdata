train <- read.csv('train_regression(2차).csv',na.strings = c(''))
glimpse(train)

#사용하지 않는 변수 제거
real_train <- train[-3]


#범주형 변수로 변경
glimpse(real_train)
real_train$OPEN_MONTH <- factor(real_train$OPEN_MONTH)
real_train$OPEN_QUARTER <- factor(real_train$OPEN_QUARTER)
real_train$SERIES <- factor(real_train$SERIES)
real_train$ORI_BOOK <- factor(real_train$ORI_BOOK)
glimpse(real_train)



#결측치 처리
aggr(real_train, sortVars=T,prop=F, cex.axis=0.45, numbers=T)
real_train$SERIES[is.na(real_train$SERIES)] <- 0
real_train <- na.omit(real_train)
aggr(real_train, sortVars=T,prop=F, cex.axis=0.45, numbers=T)
glimpse(real_train)
summary(real_train)


#최소값과 최대값의 차이가 큰 변수들에 로그를 씌워서 편차를 줄인다.
real_train <- mutate(real_train, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1), AUDI_ACC = log10(AUDI_ACC))
summary(real_train)


#학습용 데이터와 검증용 데이터 분리
sample <- sample.split(real_train$AUDI_ACC,SplitRatio = 0.80)
movie_train <- subset(real_train, sample==T)
test <- subset(real_train, sample==F)



#랜덤포레스트를 이용한 영화데이터 기계학습(선형회귀)
set.seed(222)
model <- randomForest(AUDI_ACC ~ .,data = real_train, ntree = 501, replace = TRUE, nodesize = 9,importance = TRUE)
model

glimpse(real_train)
#변수 중요도 확인 
importance(model)


#예측영화 로딩
test <- read.csv('test.csv',na.strings = c(''))

#필요한 컬럼 추출 
glimpse(test)
test <- test[-c(1,2)]
test <- test[-3]
glimpse(test)


#factor타입 동일조건 설정
test$AUDI_ACC <- NA
test
imsi <- rbind(real_train,test)
glimpse(imsi)
test <- imsi[4188:4207,]
glimpse(test)
test <- test[-12]
glimpse(test)
real_train$PRI_GENRE_NM
test$PRI_GENRE_NM


#예측데이터 정규화
test <- mutate(test, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1))
summary(test)

#관객수 예측
y_pred <- predict(model,test)
test$AUDI_ACC_PRED <- y_pred
test <- mutate(test, AUDI_ACC_PRED=10^(AUDI_ACC_PRED))
test
test$AUDI_ACC_PRED <- floor(test$AUDI_ACC_PRED)
write.csv(test,'prediction.csv',row.names = F, fileEncoding = 'cp949')
