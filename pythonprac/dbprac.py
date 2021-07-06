from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # 27017 MongoDB 포트
db = client.dbsparta  # 'dbsparta' 라는 이름의 db 생성

# insert / find / update / delete

# insert
# doc = {'name': 'bobby', 'age': 21}
# db.users.insert_one(doc)

# find
# same_ages = list(db.users.find({'age': 21}, {'_id': False}))
# user = db.users.find_one({'name':'bobby'})
# for person in same_ages:
#     print(person)

# find_one
# user = db.users.find_one({'name': 'bobby'}, {'_id': False})
# print(user)

# update
# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})

# delete
# db.users.delete_one({'name': 'bobby'})
