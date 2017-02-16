import rpy2.robjects as ro
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr

# import R's utility package
utils = rpackages.importr('utils')

# select a mirror for R packages
utils.chooseCRANmirror(ind=1) # select the first mirror in the list
if not rpackages.isinstalled("arules"):
	utils.install_packages("arules")
arules = importr("arules")


ro.r("compras <- read.transactions(file = 'ultimaTentativa.csv', format = 'single', sep = ',', cols = c(2,3))")
ro.r("rules <- apriori(data = compras, parameter = list(support=0.3, confidence=0.95))")
ro.r("inspect(head(sort(rules, by='lift'),20))")