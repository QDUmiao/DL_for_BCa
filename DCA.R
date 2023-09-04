#library(dcurves)
library(survival)
source("D:/dca.R")
source("D:/stdca.R")
df_surv <- read.csv("C:",header = T)

dim(df_surv)
str(df_surv)

DL <- coxph(Surv(TIME, Status) ~ prob, 
                  data = df_surv)
AJCC.system <- coxph(Surv(TIME, Status) ~ AJCC, data = df_surv)
DLRN <- coxph(Surv(TIME, Status) ~ rad_score+Age+N.stage+Extramural.infiltration, data = df_surv)
Clinical.model <- coxph(Surv(TIME, Status) ~ Age+N.stage+Extramural.infiltration, data = df_surv)

df_surv$DL <- c(1-(summary(survfit(DL, newdata=df_surv), times=36)$surv))
df_surv$AJCC.system <- c(1-(summary(survfit(AJCC.system, newdata=df_surv), times=36)$surv))
df_surv$DLRN <- c(1-(summary(survfit(DLRN, newdata=df_surv), times=36)$surv))
df_surv$Clinical.model <- c(1-(summary(survfit(Clinical.model, newdata=df_surv), times=36)$surv))

stdca(data=df_surv, 
      outcome="Status", 
      ttoutcome="TIME", 
      timepoint=36, 
      predictors=c("DL","AJCC.system","DLRN","Clinical.model"),  
      smooth=TRUE
)

