#훈련 전 전처리
train <- read.csv('train_regression(1차).csv')
train$OPEN_MONTH <- factor(train$OPEN_MONTH)
train$OPEN_QUARTER <- factor(train$OPEN_QUARTER)
train$SERIES <- factor(train$SERIES)
train$ORI_BOOK <- factor(train$ORI_BOOK)
glimpse(train)
summary(train)
train <- mutate(train, NAVER_CMT_NN = log10(NAVER_CMT_NN+1), NAVER_EX_PT = log10(NAVER_EX_PT+1), AUDI_ACC = log10(AUDI_ACC))

#학습용 데이터와 검증용 데이터 분리
sample <- sample.split(train$AUDI_ACC,SplitRatio = 0.80)
real_train <- subset(train, sample==T)
test <- subset(train, sample==F)


#랜덤포레스트를 이용한 영화데이터 기계학습(선형회귀)
set.seed(222)
model <- randomForest(AUDI_ACC ~ .,data = real_train, ntree = 501, replace = TRUE, nodesize = 9,importance = TRUE)




#변수중요도와 노드불순도확인
importance(model)



#검증용데이터로 예측
pred <- predict(model, test[-12])
test$AUDI_ACC_PRED <- pred
test <- test[-13]
test <- mutate(test, AUDI_ACC = 10^AUDI_ACC, AUDI_ACC_PRED = 10^pred)
write.csv(test,'prediction(1차).csv',row.names = F, fileEncoding = 'cp949')