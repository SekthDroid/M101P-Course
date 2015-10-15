__author__ = 'SekthDroid'

from pymongo import MongoClient
from bottle import route, run


@route('/')
def hello():
    # Create the connection to Mongo
    connection = MongoClient('localhost', 27017)

    # We connect to the test database
    db = connection.test

    # We will be using the names collection
    names = db.names

    # Get one element
    item = names.find_one()
    return "<b>Hello %s!</b>" % item["name"]


run(host='localhost', port=8082, debug=True)