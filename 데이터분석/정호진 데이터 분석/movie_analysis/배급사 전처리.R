train <- read.csv('imsi.csv')
glimpse(train)

#관객수 적은 배급사 정리
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='씨제이이앤엠(주)'] <- '씨제이이앤엠(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='롯데쇼핑㈜롯데엔터테인먼트'] <- '롯데쇼핑㈜롯데엔터테인먼트'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)쇼박스'] <- '(주)쇼박스'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)넥스트엔터테인먼트월드(NEW)'] <- '(주)넥스트엔터테인먼트월드(NEW)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='롯데컬처웍스(주)롯데엔터테인먼트'] <- '롯데컬처웍스(주)롯데엔터테인먼트'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='월트디즈니컴퍼니코리아 유한책임회사'] <- '월트디즈니컴퍼니코리아 유한책임회사'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='월트디즈니컴퍼니코리아(주)'] <- '월트디즈니컴퍼니코리아(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='소니픽쳐스릴리징월트디즈니스튜디오스코리아(주)'] <- '소니픽쳐스릴리징월트디즈니스튜디오스코리아(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='워너브러더스 코리아(주)'] <- '워너브러더스 코리아(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='이십세기폭스코리아(주)'] <- '이십세기폭스코리아(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='소니픽쳐스엔터테인먼트코리아주식회사극장배급지점'] <- '소니픽쳐스엔터테인먼트코리아주식회사극장배급지점'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='한국소니픽쳐스릴리징브에나비스타영화㈜'] <- '한국소니픽쳐스릴리징브에나비스타영화㈜'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='메가박스중앙(주)플러스엠'] <- '메가박스중앙(주)플러스엠'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='씨제이엔터테인먼트'] <- '씨제이엔터테인먼트'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='유니버설픽쳐스인터내셔널 코리아(유)'] <- '유니버설픽쳐스인터내셔널 코리아(유)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='CGV아트하우스'] <- 'CGV아트하우스'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='판씨네마(주)'] <- '판씨네마(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)와우픽쳐스'] <- '(주)와우픽쳐스'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)인벤트스톤'] <- '(주)인벤트스톤'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='필라멘트픽쳐스'] <- '필라멘트픽쳐스'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='오퍼스픽쳐스(유)'] <- '오퍼스픽쳐스(유)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)싸이더스'] <- '(주)싸이더스'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='씨네그루(주)다우기술'] <- '씨네그루(주)다우기술'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)제이앤씨미디어그룹'] <- '(주)제이앤씨미디어그룹'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='씨너스엔터테인먼트(주)'] <- '씨너스엔터테인먼트(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='에스케이텔레콤(주)'] <- '에스케이텔레콤(주)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='씨네그루(주)키다리이엔티'] <- '씨네그루(주)키다리이엔티'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)시너지하우스 (시너지)'] <- '(주)시너지하우스 (시너지)'
train$COMPANY_NM_R[train$PRI_COMPANY_NM=='(주)시네마서비스'] <- '(주)시네마서비스'
train$COMPANY_NM_R[is.na(train$COMPANY_NM_R)] <- '기타'
glimpse(train)
summary(train)
table(train$COMPANY_NM_R)
write.csv(train,'imsi.csv',row.names = F, fileEncoding = 'cp949')


