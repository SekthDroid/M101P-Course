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
        print_items_with_limit(docs, 10)
    except Exception as e:
        print_error(e)


def print_items_with_limit(docs, limit):
    for item in docs[:limit]:
        print(item)


def find_with_projection():
    print("Find method with projection")
    query = {"student_id": 1}
    projection = {"student_id": 1, "score": 1, "_id": 0}

    try:
        docs = scores.find(query, projection)

        print_items_with_limit(docs, 10)
    except Exception as e:
        print_error(e)

find_one()
find()
find_with_projection()