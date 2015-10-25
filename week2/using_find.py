import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores


def print_error(e):
    print("Unexpected error:", type(e), e)


def find_one():
    print("Find one method")
    query = {'student_id': 0}

    try:
        doc = scores.find_one(query)
        print doc
    except Exception as e:
        print_error(e)


def find():
    print("Find method")
    query = {"type": "exam"}

    try:
        docs = scores.find(query)

        # Only printing 10 results
        for item in docs[:10]:
            print(item)
    except Exception as e:
        print_error(e)


find_one()
find()