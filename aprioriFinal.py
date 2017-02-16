# 1- escolher um cnpj
# 2- selecionar todos os itens de compras dele
# 3- para cada item buscar todos os cnpjs relacionados
# 4- gerando uma lista de cnpj por item
# 5- uniao dessas listas vai ser a entrada pro apriori

import mysql.connector
from pandas import DataFrame
import pandas as pd
from itertools import combinations
from apyori import apriori

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="mydb")        # name of the data base


cur = db.cursor()

cnpj = "02055765000154"
data = "100010500039201500001"
query = ("select id, cnpj from licitacoes where iditemcompra in (select iditemcompra from licitacoes where cnpj = '02055765000154')")

cur.execute(query)

#data = []


for (id, cnpj) in cur:
  data.append((id, cnpj))
#print(data)

df = pd.DataFrame(data = data, columns=['id', 'cnpj'])
#print(df)

cur.close()
db.close()

results = list(apriori(df))

print(results)
