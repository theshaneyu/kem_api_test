from pymongo import MongoClient

client = MongoClient('mongodb://140.120.13.243:4444/')
db = client['database']
collection = db['kem_test_coll']

testData = {'name':'Eating', 'age':'13'}

result = collection.insert(testData)
print(result)