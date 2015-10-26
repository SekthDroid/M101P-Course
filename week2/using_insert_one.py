import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
people = db.people


def insert(person):
    print("Insert one method")

    try:
        people.insert_one(person)
    except Exception as e:
        print("Unexpected error: ", type(e), e)


john = {"name": "John Dow", "company": "Google", "interest": ["horses", "skydiving", "fencing"]}
insert(john)

dale = {"_id": "dalej", "name": "Dale J. Roberts", "interests": ["computer", "cars", "football"]}
insert(dale)