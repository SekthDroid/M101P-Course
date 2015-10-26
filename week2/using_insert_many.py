import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.tech
os = db.os


def print_items():
    query = {}
    projection = {"name": 1}
    items = [item["name"] for item in os.find(query, projection)]
    print (items)


def insert_many(items, ordered=False):
    try:
        os.insert_many(items, ordered)
    except Exception as e:
        print("Unexpected error: ", type(e), e)


print_items()

operative_systems = list()
operative_systems.append({"name": "Android"})
operative_systems.append({"_id": "windows", "name": "Windows"})
operative_systems.append({"name": "iOS"})
insert_many(operative_systems, True)

print_items()
insert_many(operative_systems, False)
