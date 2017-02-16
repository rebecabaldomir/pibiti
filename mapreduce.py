list_data = []
f = open("data/201001_CPGF.csv", "r")
data = f.read()

rows = data.split("\t")

for row in rows:
    split_row = row.split(",")
    list_data.append(split_row)
list_data = list_data[15:]

print(list_data[0:15])

arq = open("lista.txt", "w")
list_data = str(list_data)
arq.write(list_data) 
arq.close()