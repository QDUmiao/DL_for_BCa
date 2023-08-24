setwd("")
library(survminer)
library(survival)
library(sva)
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
library(e1071)

dt_adj <- read_csv('KM.csv')
units(dt_adj$TIME) <- "Month"
dt_adj$RISK1 <- factor(dt_adj$risk2,labels=c("Low Risk", "High Risk"))
dt_train_pre <- dt_adj[c(1:620),]
dt_test_pre <- dt_adj[c(621:874),]
dt_train_pre <- dt_train_pre[,c(-1,-2)]
dt_test_pre <- dt_test_pre[,c(-1,-2)]
colnames(dt_test_pre) <- colnames(dt_train_pre)

fit <- survfit(Surv(TIME,Status)~ risk2, data = dt_train_pre)
fit
summary(fit)
ggsurvplot(fit, # 创建的拟合对象
           data = dt_train_pre, # 指定变量数据来源
           conf.int = TRUE, # 显示置信区间
           fun = "cumhaz",
           xlim =c(0,60), break.x.by = 12, ylim =c(0,1), break.y.by = 0.2,
           pval = TRUE, label.x = 3,label.y = 38,# 添加P值,
           risk.table = TRUE, #不同时间点风险人数表
           legend.labs = c("Low Risk", "High Risk"), # ָ??ͼ????????ǩ
           xlab = "Follow up time(months)", # ָ??x????ǩ
           ylab = "Cumulative recurrence rate", # ָ??x????ǩ
           surv.median.line = "hv", # 添加中位生存时间线
           add.all = F) # 添加总患者生存曲线        
#log-rank ?????????ʲ???
survdiff(Surv(TIME,Status)~ RISK1, dt_train_pre)
#����?Ƚ?
pairwise_survdiff(Surv(TIME,Status)~ RISK1, dt_train_pre,p.adjust.method= "BH")

#??֤??
fit2 <- survfit(Surv(TIME,Status)~ RISK1, data = dt_test_pre)
fit2
summary(fit2)

#????????
ggsurvplot(fit2,#ggsurvpl#创建�对象
           data = dt_test_pre, # 指定变量数据来源
           conf.int = TRUE, # 显示置信区间
           fun = "cumhaz",
           xlim =c(0,60), break.x.by = 12, ylim =c(0,1), break.y.by = 0.2,
           pval = TRUE, label.x = 3,label.y = 38,# 添加P值,
           risk.table = TRUE, #不同时间点风险人数表
           legend.labs = c("Low Risk", "High Risk"), # ָ??ͼ????????ǩ
           xlab = "Follow up time(months)", # ָ??x????ǩ
           ylab = "Cumulative recurrence rate", # ָ??x????ǩ
           surv.median.line = "hv", # 添加中位生存时间线
           add.all = F) # 添加总患者生存曲线     ʲ???
survdiff(Surv(TIME,Status)~ RISK1, dt_test_pre)
#����?Ƚ?
pairwise_survdiff(Surv(TIME,Status)~ RISK1, dt_test_pre,p.adjust.method = "BH")

