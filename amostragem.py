import csv
from collections import Counter  
import itertools  
import sys  

list_data = []
f = open("SIASG_ITENS_LIC.CSV", "r")
fwrite  = open("teste2.csv", "w")
reader = csv.reader(f, delimiter="\n")
writer = csv.writer(fwrite, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)
i = 0
for row in reader:
	writer.writerow(row)
	i = i + 1
	if (i == 100):
		break



#rows = data.split("\n")
##rows = rows[0:100]
#print(rows)

#rows = data.split("\t")

#for row in rows:
#    split_row = row.split(",")
#    list_data.append(split_row)
#list_data = list_data[15:]

 