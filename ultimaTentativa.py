import mysql.connector
from pandas import DataFrame
import pandas as pd
from itertools import combinations

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="mydb")        # name of the data base


cur = db.cursor()

query = ("select iditemcompra, cnpj from licitacoes where iditemcompra in (select iditemcompra from licitacoes where cnpj = '00761025000108')  limit 50")

cur.execute(query)

data = []


for (iditemcompra, cnpj) in cur:
  data.append((iditemcompra, cnpj))
#print(data)

df = pd.DataFrame(data = data, columns=['iditemcompra', 'cnpj'])
#print(df)

cur.close()
db.close()

df.to_csv('ultimaTentativa.csv')