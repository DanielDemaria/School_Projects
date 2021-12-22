## Daniel DeMaria

### Statistical Learning Project

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


```markdown
lm1 <- lm(rating ~ ., mov_train)


lm2 <- lm(rating ~ popularity + genre + mood + I(popularity * genre)
+ I(popularity * mood) + I(genre * mood), mov_train)



lm3 <- lm(rating ~ popularity + genre + mood + I(popularity^2)
+ I(genre^2) + I(popularity * genre) + I(popularity *mood)
+ I(genre * mood), mov_train)
```
!(https://github.com/DanielDemaria/School_Projects/blob/main/images/00000f.png)





