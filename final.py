import os, os.path
import cherrypy
import rpy2.robjects as ro
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
import mysql.connector
from APIBanco import *
from APIRegras import *


class AprioriApp(object):
	@cherrypy.expose
	def index(self):
		return open('interface.html')


@cherrypy.expose
class AprioriAPI(object):
	@cherrypy.tools.json_out()
	def GET(self, cnpj):
		data = APIBanco().search(cnpj)
		regras = APIRegras().applyApriori()
		cnpjs = APIBanco().searchCNPJS(regras)
		retorno = str(cnpjs)
		return cnpjs

if __name__ == '__main__':
	conf = {
		'/': {
			'tools.sessions.on': True,
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/cnpj': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.response_headers.on': True,
			'tools.response_headers.headers': [('Content-Type', 'application/json')],
		},
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './public'
		}
	}
	webapp = AprioriApp()
	webapp.cnpj = AprioriAPI()
	cherrypy.quickstart(webapp, '/', conf)