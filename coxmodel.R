library(tidyverse)
library(caret)
library(pROC)
library(glmnet)
library(DMwR2)
library(rmda)
library(ggpubr)
library(ModelGood)
library(rms)
library(mRMRe)
library(DescTools)
library(Boruta)
library(sva)
library(e1071)
library(survcomp)
library(timeROC)
library(survival)
library(pec)
library(riskRegression)
library(rms)
library(Hmisc)

setwd("C:")
dt_train_pre<- read.csv('train.csv')
dt_test_pre <- read.csv('test.csv')
colnames(dt_test_pre) <- colnames(dt_train_pre)
#fix(dt_train_pre)
dt_adj_train <- dt_train_pre[,c(-1,-2)]
dt_adj_test <- dt_test_pre[,c(-1,-2)]


res.cox1<-coxph(Surv(TIME,Status)~.,data=dt_train_pre)
summary(res.cox1)

cindex1 <- concordance.index(predict(res.cox1, newdata = dt_train_pre),surv.time = dt_train_pre$TIME,surv.event = dt_train_pre$Status,method="noether")
cindex1$c.index; cindex1$lower; cindex1$upper
pre1 <- predict(res.cox1, newdata = dt_train_pre)
pre1 <- data.frame(pre1)
#fix(pre1)
write.csv(pre1, 'pred-train.csv')
dt_train_pre <- bind_cols(dt_train_pre, pre1)
surroc <- timeROC(T = dt_train_pre$TIME,delta = dt_train_pre$Status,marker = dt_train_pre$pre1, cause=1,times=c(6,12,24,36,48),iid = TRUE)
surroc$AUC

cindex2 <- concordance.index(predict(res.cox1, newdata = dt_test_pre), surv.time = dt_test_pre$TIME,surv.event = dt_test_pre$Status,method="noether")
cindex2$c.index; cindex2$lower; cindex2$upper
pre2 <- predict(res.cox1, newdata = dt_test_pre)
pre2 <- data.frame(pre2)
#fix(pre2)
write.csv(pre2, 'pred-test.csv')
dt_test_pre <- bind_cols(dt_test_pre, pre2)
surroc2 <- timeROC(T = dt_test_pre$TIME,delta = dt_test_pre$Status,marker = dt_test_pre$pre2, cause=1,times=c(6,12,24,36,48),iid = TRUE)
surroc2$AUC
#IBS
Models <- list("Model1"= coxph(Surv(TIME,Status)~pre1, data=dt_train_pre, x=TRUE, y=TRUE))
p <- pec(object = Models,formula=Surv(TIME,Status)~pre1, data=dt_train_pre, splitMethod="Boot632plus",
         B=1000,reference = FALSE)
print(p, times=seq(5,60,5))

Models2 <- list("Model2"= coxph(Surv(TIME,Status)~pre2, data=dt_test_pre, x=TRUE, y=TRUE))
p2 <- pec(object = Models2,formula=Surv(TIME,Status)~pre2, data=dt_test_pre, splitMethod="Boot632plus",
          B=1000,reference = FALSE)
print(p2, times=seq(5,60,5))