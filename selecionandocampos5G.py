import csv
#import MySQLdb

f = open("SIASG_ITENS_LIC.CSV", "r")
#f = open("teste.csv", "r")
#abre arquivo de teste com 100 registros

#dados que seram passados para o bd:


# Modalidade_Licitacao->(data[1:2])
# Data_Referencia_Compra->(data[5:6])
# Identificacao_ItemCompra->(data[8:9])
# Cpf_Cnpj_Fornecedor->(data[23:24])
# Valor_Total_Homologado->(data[31:32])
# Poder_Unidade->(data[41:42])

line = []
i=0
while f.readline() != '':
	row = f.readline()
	data = row.split("\xac")
	line.append((data[8:9], data[5:6], data[23:24], data[41:42], data[1:2], data[31:32]))
	i=i+1

tam = len(line) - 1
line = line[1:tam]
print(line[0:1])
print(len(line))

#db = MySQLdb.connect(host="localhost", 
#                     user="root",  
#                     passwd="root",  
#                     db="mydb") 

#cur = db.cursor()
#
#query = ("INSERT INTO licitacoes (iditemcompra, datareferencia, cnpj, poderunidade, modalidade, valorpreco) VALUES (%s, %s, %s, %s, %s, %s)")


#cur.executemany(query, line)

#db.commit()

#db.close()
