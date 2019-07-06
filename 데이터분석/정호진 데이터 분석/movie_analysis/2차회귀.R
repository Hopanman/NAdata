train <- read.csv('train_regression(2차).csv')
glimpse(train)

real_train <- train[-3]

glimpse(real_train)

real_train$OPEN_MONTH <- factor(real_train$OPEN_MONTH)
real_train$OPEN_QUARTER <- factor(real_train$OPEN_QUARTER)
real_train$SERIES <- factor(real_train$SERIES)
real_train$ORI_BOOK <- factor(real_train$ORI_BOOK)
glimpse(real_train)
