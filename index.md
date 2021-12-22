## Statistical Learning

```markdown
library(boot)
library(class)
library(FNN)
library(caret)
library(MASS)
library(ggplot2)
library(tidyverse)
library(knitr)


#read in data/load in packages 

mov_test <- read.csv("mov_eval.csv", na.strings="NA")

mov_train <- read.csv("mov_train.csv", na.strings="NA")

wisc_train <- read.csv("wisc.csv", na.strings="NA")

wisc_test <- read.csv("wisc_eval.csv", na.strings="NA")
```
* Creating 3 linear regression models

```markdown
lm1 <- lm(rating ~ ., mov_train)

lm2 <- lm(rating ~ popularity + genre + mood + I(popularity * genre)
+ I(popularity * mood) + I(genre * mood), mov_train)
+ 
lm3 <- lm(rating ~ popularity + genre + mood + I(popularity^2)
+ I(genre^2) + I(popularity * genre) + I(popularity * mood)
+ I(genre * mood), mov_train)
```
* QQnorm plots to show that the irreducible errors in all 3 models are not 
normally distributed. 

```markdown
par(mfrow=c(2,2))
qqnorm(lm1$residuals)
qqline(lm1$residuals)

qqnorm(lm2$residuals)
qqline(lm2$residuals)

qqnorm(lm3$residuals)
qqline(lm3$residuals)
```
![This is an image](https://github.com/DanielDemaria/School_Projects/blob/gh-pages/images/00000f.png?raw=true)
