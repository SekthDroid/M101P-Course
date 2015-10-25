import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores


def find():
    print("Find with Sort Skip Limit")
    query = {}

    try:
        cursor = scores.find(query).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.DESCENDING)]).skip(
            4).limit(2)

        for item in cursor:
            print(item)
    except Exception as e:
        print("Unexpected error: ", type(e), e)


find()