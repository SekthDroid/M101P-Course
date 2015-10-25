import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores


def find_one():
    print("Find one method")
    query = {'student_id': 0}

    try:
        doc = scores.find_one(query)
        print doc
    except Exception as e:
        print("Unexpected error:", type(e), e)


find_one()