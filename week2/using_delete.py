import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores


def find_for_student(student_id):
    query = {"student_id": student_id}
    try:
        docs = scores.find(query)
        return [doc for doc in docs]
    except Exception as e:
        print("Unexpected error:", type(e), e)


def remove_one_for_student(student_id):
    query = {"student_id": student_id}
    try:
        result = scores.delete_one(query)
        return result.deleted_count
    except Exception as e:
        print("Unexpected error:", type(e), e)


def remove_all_for_student(student_id):
    query = {"student_id": student_id}
    try:
        result = scores.delete_many(query)
        return result.deleted_count
    except Exception as e:
        print("Unexpected error:", type(e), e)


if __name__ == "__main__":
    items = find_for_student(2)
    print("There is %d items for student" % len(items))
    print(items)

    removed = remove_one_for_student(2)
    print("Removed %d items" % removed)

    items = find_for_student(2)
    print("There is %d items for student" % len(items))
    print(items)

    removed = remove_all_for_student(2)
    print("Removed %d items" % removed)