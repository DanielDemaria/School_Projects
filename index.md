## Daniel DeMaria


### Markdown

```markdown
lm1 <- lm(rating ~ ., mov_train)
summary(lm1)


lm2 <- lm(rating ~ popularity + genre + mood + I(popularity * genre)
+ I(popularity * mood) + I(genre * mood), mov_train)
summary(lm2)


lm3 <- lm(rating ~ popularity + genre + mood + I(popularity^2)
+ I(genre^2) + I(popularity * genre) + I(popularity *mood)
+ I(genre * mood), mov_train)
summary(lm3)


```


