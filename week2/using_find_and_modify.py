import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
counters = db.counters


def increment(counter_name):
    try:
        counter = counters.find_one_and_update(
            filter={"type": counter_name},
            update={"$inc": {"value": 1}},
            upsert=True,
            return_document=pymongo.ReturnDocument.AFTER
        )

        return counter["value"]
    except Exception as e:
        print("Unexpected error:", type(e), e)


if __name__ == "__main__":
    for i in range(10):
        print(increment("counter1"))

    for i in range(10):
        print(increment("counter2"))