import csv
import MySQLdb
f = open("teste.csv", "r").read()
fwrite  = open("apenasnecesario.csv", "w")

#dados que seram passados para o arquivo apenasnecessario.csv:

#identificacao item compra 8 OK
#data de referencia 5 OK
#data de resultado 6 OK
#cpf/cnpj do fornecedor 23 OK
#poder unidade 41
#modalidade 1 OK
#valor preco unidade homologacao(se tiver preenchido eh pq venceu a lic) 32 OK

line = []
rows = f.split("\n")
i=0
for row in rows:
	data = row.split("\xac")
	line.append((data[8:9], data[5:6], data[23:24],
	data[41:42], data[1:2], data[31:32]))
	i=i+1
print(line[0:1])
tam = len(line) - 1
line = line[0:tam]

#print(Valor_Total_Homologado)

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="mydb")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need

cur = db.cursor()

# Use all the SQL you like
# for(i = 0; i < Modalidade_Licitacao.size(); i = i+1):
# 	cur.execute("INSERT INTO licitacoes VALUES ("Modalidade_Licitacao[i],
# 	Data_Referencia_Compra[i],
# 	Data_Resultado_Compra[i],
# 	Identificacao_ItemCompra[i],
# 	Cpf_Cnpj_Fornecedor[i],
# 	Valor_Total_Homologado[i],
# 	Poder_Unidade[i]")")

query = ("INSERT INTO licitacoes (iditemcompra, datareferencia, cnpj, poderunidade, modalidade, valorpreco) VALUES (%s, %s, %s, %s, %s, %s)")



#data = (Identificacao_ItemCompra[0], Data_Referencia_Compra[0], Cpf_Cnpj_Fornecedor[0],
 #Poder_Unidade[0], Modalidade_Licitacao[0], Valor_Total_Homologado[0])
#print(data)

#cur.execute(query, data)

#cur.executemany(query, line)

db.commit()

# print all the first cell of all the rows

#for row in cur.fetchall():
#    print row[0]

db.close()