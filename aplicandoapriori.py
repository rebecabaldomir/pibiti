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

#data = "100010500039201500001"
query = ("select iditemcompra, cnpj from licitacoes")

cur.execute(query)

data = []


for (id, cnpj) in cur:
  data.append((id, cnpj))
#print(data)

df = pd.DataFrame(data = data, columns=['id', 'cnpj'])
print(df)

cur.close()
db.close()

results = list(apriori(df))

print(results)

# def get_support(df):
#     pp = []
#     for cnum in range(1, len(df.columns)+1):
#         for cols in combinations(df, cnum):
#             s = df[list(cols)].all(axis=1).sum()
#             pp.append([",".join(cols), s])
#     sdf = pd.DataFrame(pp, columns=["Pattern", "Support"])
#     return sdf

# s = get_support(df)
# print(s)