from pymongo import MongoClient

client = MongoClient('mongodb://140.120.13.243:4444/')
db = client['database']
collection = db['dataset']

testData = {'name':'Shane', 'age':'24'}

result = collection.insert(testData)
print(result)