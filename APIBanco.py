import mysql.connector
import pandas as pd
from pandas import DataFrame
import csv

class APIBanco(object):

	def __init__(self):
		self.connect()

	
	def connect(self):
		self.db = mysql.connector.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     passwd="root",  # your password
	                     db="mydb")        # name of the data base
		
	
	def search(self, cnpj):
		self.cur = self.db.cursor()

		query = ("select iditemcompra, cnpj from licitacoes where iditemcompra in (select iditemcompra from licitacoes where cnpj = '" + cnpj + "')  limit 50")

		self.cur.execute(query)

		return self.format()

	def searchCNPJS(self, regras):
		
		cnpjs = tuple(regras[2].levels)
		dados = []
		for cnpj in cnpjs:
			dados.append(cnpj.replace("{", "").replace("}",""))
		#print(dados)
		#self.format()
		return dados
	
	def format(self):
		data = []
		for (iditemcompra, cnpj) in self.cur:
			data.append((iditemcompra, cnpj))
		#df = pd.DataFrame(data = data, columns=['id', 'cnpj'])
		with open('dadosParaAplicarRegras.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerows(data)
		self.close()
		return data

	def close(self):
		self.cur.close()
		self.db.close()

