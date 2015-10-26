import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.tech
os = db.os

if __name__ == "__main__":
    os.drop()

    os.update_one({"os": "Android"}, {"$set": {"color": "green"}}, upsert=True)
    os.update_many({"os": "iOS"}, {"$set": {"color": "white"}}, upsert=True)
    os.replace_one({"os": "Windows"}, {"color": "blue"}, upsert=True)

    android = os.find_one({"os": "Android"})
    print(android)

    ios = os.find_one({"os": "iOS"})
    print(ios)

    # This will print  None
    windows = os.find_one({"os": "Windows"})
    print(windows)

    # In order to be able to use upsert with replace_one, we need to do
    os.replace_one({"os":"Windows"}, {"os":"Windows", "color":"blue"}, upsert=True)

    windows = os.find_one({"os":"Windows"})
    print(windows)