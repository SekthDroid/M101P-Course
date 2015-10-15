__author__ = 'SekthDroid'

from pymongo import MongoClient

# Create the connection to Mongo
connection = MongoClient('localhost', 27017)

# We connect to the test database
db = connection.test

# We will be using the names collection
names = db.names

# Get one element
item = names.find_one()

# Print the name attr
print(item['name'])