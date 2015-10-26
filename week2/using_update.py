from datetime import datetime
import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores


def find(student_id):
    print("Find student with id %d" % student_id)
    query = {"student_id": student_id}
    try:
        item = scores.find_one(query)
        return item
    except Exception as e:
        print("Unexpected error: ", type(e), e)
        return None


def update_with_review_date(student_id, review):
    print("Update student with new review date")

    query = {"student_id": student_id}
    update_value = {"$set": {"review_date": review}}
    try:
        result = scores.update_one(query, update_value)
        return result.matched_count
    except Exception as e:
        print("Unexpected error: ", type(e), e)
        return -1


def update_all_with_review_date(review):
    print("Update all students with new review date")
    query = {}
    update_value = {"$set": {"review_date": review}}
    try:
        result = scores.update_many(query, update_value)
        return result.matched_count
    except Exception as e:
        print("Unexpected error: ", type(e), e)
        return -1


def find_all():
    try:
        students = scores.find()
        return students
    except Exception as e:
        print("Unexpected error: ", type(e), e)
        return {}


if __name__ == "__main__":
    print("Updating just one student")
    student = find(2)
    print(student)
    review_date = datetime.utcnow()
    updated = update_with_review_date(student["student_id"], review_date)
    print("Updated %d documents" % updated)
    print(find(2))

    print("Updating all students")
    updated = update_all_with_review_date(review_date)
    print("Updated %d documents" % updated)
    for item in find_all()[:10]:
        print(item)