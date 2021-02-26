from logging import exception
from flask import Flask
from flask import request

from flask import jsonify
from flask.json import jsonify

from werkzeug.datastructures import Accept

from utility import Utility

obj=Utility()


app = Flask(__name__)
books=[
    {'name':'alittlemermaid',
    'writer':'not me',
    'weight':'who cares'
    },
    {'name':'Harry potter',
    'writer':'j.k.rowling',
    'weight':'not sure'}
]


@app.route('/', methods=['GET'])
def home():
    return " Home page Nothing is here"

@app.route('/books', methods=['GET'])
def showbooks():
    return jsonify(books)

@app.route('/clan', methods=['POST'])
def change():
    obj.getdata(request.get_json(force=True))
    return str(obj.changelan())

@app.route('/robj', methods=['GET'])
def reobj():
    return jsonify(obj.robj())

@app.route('/alan',methods=['GET'])
def rlan():
    return jsonify(obj.All_Languages())

@app.route('/nl',methods=['GET'])
def nlan():
    return str(obj.nlan())
  
    



if __name__ == '__main__':
    app.run(debug=True)