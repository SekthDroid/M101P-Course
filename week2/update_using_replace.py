from datetime import datetime
import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores


def clear_reviews():
    query = {"review_date": {"$exists": True}}
    update_value = {"$unset": {"review_date": 1}}
    try:
        result = scores.update_many(query, update_value)
        return result.matched_count
    except Exception as e:
        print("Unexpected Error: ", type(e), e)
        return -1


def find(student_id):
    query = {"student_id": student_id}

    try:
        found_student = scores.find_one(query)
        return found_student
    except Exception as e:
        print("Unexpected Error: ", type(e), e)
        return None


def replace_student(the_student):
    query = {"_id": the_student["_id"]}
    try:
        scores.replace_one(query, the_student)
    except Exception as e:
        print("Unexpected Error: ", type(e), e)


if __name__ == "__main__":
    cleared = clear_reviews()
    print("Reviews cleared: %d" % cleared)

    student = find(1)
    print(student)

    student["review_date"] = datetime.utcnow()
    replace_student(student)

    student = find(1)
    print(student)
