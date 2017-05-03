library(arules)
library(arulesViz)
install.packages("arulesViz")
??read.transactions
compras <- read.transactions(file = 'ultimaTentativa.csv', format = 'single', sep = ',', cols = c(2,3))
rules <- apriori(data = compras, parameter = list(support=0.3, confidence=0.95))
plot(rules)
inspect(head(sort(rules, by="lift"),20))
