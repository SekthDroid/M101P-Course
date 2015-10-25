import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.reddit
stories = db.stories


def find():
    print("Find with regex within Reddit db")
    query = {'title': {'$regex': 'android|google', '$options': 'i'}}
    projection = {'title': 1, "_id": 0}

    try:
        cursor = stories.find(query, projection)
        for doc in cursor:
            print(doc)
    except Exception as e:
        print "Unexcepted error:", type(e), e

find()