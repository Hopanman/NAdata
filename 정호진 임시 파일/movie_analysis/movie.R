library(tidyverse)
install.packages('corrplot')
library(corrplot)

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

movie[1:4213,] %>% group_by(DIRECTOR) %>% summarise(director_n=n()) %>% arrange(desc(director_n)) %>% filter(!is.na(DIRECTOR)) %>% head(20)

sum(movie$AUDI_ACC <= 10000)

mean(movie$AUDI_ACC)

median(movie$AUDI_ACC)
table(movie$ORI_BOOK)
factor(movie$ORI_BOOK)

movie$ORI_BOOK <- factor(movie$ORI_BOOK)

glimpse(movie)

book <- ggplot(movie, aes(x=ORI_BOOK, y=AUDI_ACC, fill=ORI_BOOK)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='원작도서유무에 따른 관객수 비교', x='원작도서유무', y='관객수')

glimpse(movie)

sum(is.na(movie$AWARDS))
table(movie$AWARDS)
movie$AWARDS <- factor(movie$AWARDS)

glimpse(movie)

ggplot(movie, aes(x=AWARDS, y=AUDI_ACC, fill=AWARDS)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='수상여부에 따른 관객수 비교', x='수상여부', y='관객수')

sum(is.na(movie$SERIES))

table(movie$SERIES)
movie$SERIES <- factor(movie$SERIES)
glimpse(movie)

ggplot(movie, aes(x=SERIES, y=AUDI_ACC, fill=SERIES)) + geom_boxplot() + scale_y_continuous(breaks=c(0,5000000,10000000,15000000), labels=c('없음','오백만명','천만명','천오백만명')) + theme_classic() + theme(legend.position = 'none') + labs(title='시리즈물여부에 따른 관객수 비교', x='시리즈물여부', y='관객수')

