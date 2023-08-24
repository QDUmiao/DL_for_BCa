#IBS
library(pec)
library(riskRegression)
library(rms)
library(Hmisc)
setwd("C:")
dt_train_pre<- read.csv('IBS_test.csv')

Models <- list("Model1"= coxph(Surv(TIME,Status)~DL, data=dt_train_pre, x=TRUE, y=TRUE),
               "Model2"= coxph(Surv(TIME,Status)~AJCC, data=dt_train_pre, x=TRUE, y=TRUE),
               "Model3"= coxph(Surv(TIME,Status)~clinical, data=dt_train_pre, x=TRUE, y=TRUE),
               "Model4"= coxph(Surv(TIME,Status)~nomogram, data=dt_train_pre, x=TRUE, y=TRUE))
p <- pec(object = Models,formula=Surv(TIME,Status)~DL, data=dt_train_pre, splitMethod="Boot632plus",
         B=1000,reference = FALSE)
print(p, times=seq(5,60,5))

opar <- par(no.readonly=TRUE)
par(mfrow = c(1, 1))

plot(p,type="l",smooth=TRUE,legend = FALSE,xlim=c(0,60),axis1.at=seq(0,60,12), ylim=c(0,0.4),
     xlab="Follow-up Time (months)", ylab="Prediction error",col = c("MediumPurple", "Red", "Yellow", "Green"),
     lwd = c(3,3,3,3),lty = c(1,1,1,1))
legend("topleft", c("DL", "AJCC", "Clinical Model", "nomogram"),
       lty = c(1,1,1,1), lwd = c(3,3,3,3), col = c("MediumPurple", "Red", "Yellow", "Green"), bty = "n")
