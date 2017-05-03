from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

# To run
# $ export FLASK_APP=helloFlask.py
# $ flask run
# http://127.0.0.1:5000/