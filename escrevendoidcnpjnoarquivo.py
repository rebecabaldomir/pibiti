import mysql.connector
from pandas import DataFrame
import pandas as pd
from itertools import combinations

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="mydb")        # name of the data base


cur = db.cursor()

query = (" select iditemcompra, cnpj from licitacoes where iditemcompra = '100010500039201500001' ")

cur.execute(query)

data = []


for (id, cnpj) in cur:
  data.append((id, cnpj))
#print(data)

df = pd.DataFrame(data = data, columns=['id', 'cnpj'])
#print(df)

cur.close()
db.close()

df.to_csv('apenasnecessario.csv')