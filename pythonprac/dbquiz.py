from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# movie = db.movies.find_one({'title': '매트릭스'})
# print(movie['star'])

# movie = db.movies.find_one({'title': '매트릭스'})
# star = movie['star']
# movies = db.movies.find({'star': star})
#
# for movie in movies:
#     print(movie['title'])

db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})

