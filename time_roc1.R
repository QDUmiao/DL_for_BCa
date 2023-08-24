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
setwd("C:")

dt_adj <- read_csv('timeroc_test.csv')

opar <- par(no.readonly=TRUE)

par(mar=c(4, 4, 1, 0.5), xpd=TRUE)
par(pin=c(3,3))
par(mfrow = c(1, 1))
plot(dt_adj$Time, dt_adj$DL.model,type = "l",col = "MediumPurple", xlab="Time after surgery (months)", ylab="Area under the ROC curve",
     xaxt = "n", ylim = c(0,1), pch = 16,lwd = 2,lty=1, cex.axis =1.2,cex.lab = 1.2)
axis(1,at=seq(0,36,12))
lines(dt_adj$Time, dt_adj$Clinical.model,type = "l",col = "Red",lwd = 2,lty=1)
lines(dt_adj$Time, dt_adj$AJCC.system,type = "l",col = "Green",lwd = 2,lty=1)
lines(dt_adj$Time, dt_adj$DLRN,type = "l",col = "Yellow",lwd = 2,lty=1)

legend('right',inset=c(-0.5,0), c("DLRN","DL.model","Clinical.model","AJCC.system"),
       lty = c(1,1,1,1), lwd = c(1,1,1,1), col = c("Yellow","MediumPurple",  "Red", "Green"), bty = "n",cex = 0.5)

