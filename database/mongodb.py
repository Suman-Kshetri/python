from pymongo import MongoClient  # type: ignore

# connection to the database
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]  # database name
collection = db["students"]  # collection name(table name)

# inserting single document
student1 = {"name": "John Doe", "age": 20, "grade": "A"}
collection.insert_one(student1)

# inserting multiple documents
students = [
    {"name": "Jane Doe", "age": 22, "grade": "B"},
    {"name": "Alice Smith", "age": 19, "grade": "A"},
    {"name": "Bob Johnson", "age": 21, "grade": "C"},
]
collection.insert_many(students)

# querying find all students

for data in collection.find():
    print(data)

# querying find students with grade A
for data in collection.find({"grade": "A"}):
    print(data)

# age greater than 20
for data in collection.find({"age": {"$gt": 20}}):
    print(data)

# list databases
print(client.list_database_names())

# delete database name school
client.drop_database("school")

# list collections
print(db.list_collection_names())

# delete collection
collection.drop()


print(db.list_collection_names())
