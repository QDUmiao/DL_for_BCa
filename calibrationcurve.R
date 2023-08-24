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
setwd("C:")
dt_train_pre1 <- read_csv('pred-trainDLRN.csv')
dt_test_pre1 <- read_csv('pred-testDLRN.csv')
dt_train_pre2 <- read_csv('pred-trainDL.csv')
dt_test_pre2 <- read_csv('pred-testDL.csv')
dt_train_pre3 <- read_csv('pred-trainclinical.csv')
dt_test_pre3 <- read_csv('pred-testclinical.csv')
dt_train_pre4 <- read_csv('pred-trainAJCC.csv')
dt_test_pre4 <- read_csv('pred-testAJCC.csv')

# Calibration plot
#DLRN
units(dt_train_pre1$TIME) <- "Month"
dd=datadist(dt_train_pre1)
options(datadist="dd")
f1 <- cph(Surv(dt_train_pre1$TIME,dt_train_pre1$Status==1)~rad_score+Age+N.stage+Extramural.infiltration, data=dt_train_pre1, x=TRUE, y=TRUE, surv = TRUE, time.inc = 36)
cal1 <- calibrate(f1, cmethod = "KM", method="boot",u=36,m=100,B=1000)

units(dt_test_pre1$TIME) <- "Month"
dd=datadist(dt_test_pre1)
options(datadist="dd")
f2 <- cph(Surv(dt_test_pre1$TIME,dt_test_pre1$Status==1)~rad_score+Age+N.stage+Extramural.infiltration, data=dt_test_pre1, x=TRUE, y=TRUE, surv = TRUE, time.inc = 36)
cal2 <- calibrate(f2, cmethod = "KM", method="boot",u=36,m=50,B=1000)
#DL
units(dt_train_pre2$TIME) <- "Month"
dd=datadist(dt_train_pre2)
options(datadist="dd")
f3 <- cph(Surv(dt_train_pre2$TIME,dt_train_pre2$Status==1)~prob, data=dt_train_pre2, x=TRUE, y=TRUE, surv = TRUE, time.inc = 36)
cal3 <- calibrate(f3, cmethod = "KM", method="boot",u=36,m=100,B=1000)

units(dt_test_pre2$TIME) <- "Month"
dd=datadist(dt_test_pre2)
options(datadist="dd")
f4 <- cph(Surv(dt_test_pre2$TIME,dt_test_pre2$Status==1)~prob, data=dt_test_pre2, x=TRUE, y=TRUE, surv = TRUE, time.inc = 36)
cal4 <- calibrate(f4, cmethod = "KM", method="boot",u=36,m=50,B=1000)
#clinical
units(dt_train_pre3$TIME) <- "Month"
dd=datadist(dt_train_pre3)
options(datadist="dd")
f5 <- cph(Surv(dt_train_pre3$TIME,dt_train_pre3$Status==1)~Age+N.stage+Extramural.infiltration, data=dt_train_pre3, x=TRUE, y=TRUE, surv = TRUE, time.inc = 36)
cal5 <- calibrate(f5, cmethod = "KM", method="boot",u=36,m=100,B=1000)

units(dt_test_pre3$TIME) <- "Month"
dd=datadist(dt_test_pre3)
options(datadist="dd")
f6 <- cph(Surv(dt_test_pre3$TIME,dt_test_pre3$Status==1)~Age+N.stage+Extramural.infiltration, data=dt_test_pre3, x=TRUE, y=TRUE, surv = TRUE, time.inc = 36)
cal6 <- calibrate(f6, cmethod = "KM", method="boot",u=36,m=50,B=1000)
#AJCC
units(dt_train_pre4$TIME) <- "Month"
dd=datadist(dt_train_pre4)
options(datadist="dd")
f7 <- cph(Surv(dt_train_pre4$TIME,dt_train_pre4$Status==1)~AJCC, data=dt_train_pre4, x=TRUE, y=TRUE, surv = TRUE, time.inc =36)
cal7 <- calibrate(f7, cmethod = "KM", method="boot",u=36,m=100,B=1000)

units(dt_test_pre4$TIME) <- "Month"
dd=datadist(dt_test_pre4)
options(datadist="dd")
f8 <- cph(Surv(dt_test_pre4$TIME,dt_test_pre4$Status==1)~AJCC, data=dt_test_pre4, x=TRUE, y=TRUE, surv = TRUE, time.inc = 36)
cal8 <- calibrate(f8, cmethod = "KM", method="boot",u=36,m=50,B=1000)

#校准曲线训练集
opar <- par(no.readonly=TRUE)
par(mfrow = c(1, 2))

plot(cal1, errbar.col = "Yellow",lwd = 2,lty=2, cex.axis =1.2,
     cex.lab = 1.2,xlab="Model predicted survival probability", ylab="Observed survival (probability)",
     xlim = c(0,1),ylim = c(0,1), subtitles = FALSE)
lines(cal1[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "Yellow",pch = 16)
par(new=TRUE)
lines(cal3[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "MediumPurple",pch = 16)
par(new=TRUE)
lines(cal5[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "Red",pch = 16)
par(new=TRUE)
lines(cal7[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "Green",pch = 16)
par(new=TRUE)
legend("topleft", c("DLRN","DL","Clinical.model","AJCC.system"),
       lty = c(1,1,1,1), lwd = c(2,2,2,2), col = c("Yellow","MediumPurple","Red","Green"), bty = "n")
abline(0,1,col="black",lty=2,lwd=1)

#校准曲线验证集
plot(cal2, errbar.col = "Yellow",lwd = 2,lty=2, cex.axis =1.2,
     cex.lab = 1.2,xlab="Model predicted survival probability", ylab="Observed survival (probability)",
     xlim = c(0,1),ylim = c(0,1), subtitles = FALSE)
lines(cal2[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "Yellow",pch = 16)
par(new=TRUE)
lines(cal4[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "MediumPurple",pch = 16)
par(new=TRUE)
lines(cal6[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "Red",pch = 16)
par(new=TRUE)
lines(cal8[,c("mean.predicted","KM")],type = "b",lwd = 2,col = "Green",pch = 16)
par(new=TRUE)
legend("topleft", c("DLRN","DL","Clinical.model","AJCC.system"),
       lty = c(1,1,1,1), lwd = c(2,2,2,2), col = c("Yellow","MediumPurple","Red","Green"), bty = "n")
abline(0,1,col="black",lty=2,lwd=1)

#列线图
surv <- Survival(f7)
nom <- nomogram(f7, fun = list(function(x) surv(36,x),function(x) surv(60,x)), fun.at = c(0.01, 0.2, 0.5,0.8,0.9,.99), funlabel = c("3-years Survivsl Probability", "5-years Survivsl Probability"), lp = F)
plot(nom)
