import os, os.path
import cherrypy
import rpy2.robjects as ro
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
import mysql.connector
from APIBanco import *
from APIRegras import *


data = APIBanco().search("00761025000108")
regras = APIRegras().applyApriori()
cnpjs = APIBanco().searchCNPJS(regras)
retorno = str(cnpjs)
