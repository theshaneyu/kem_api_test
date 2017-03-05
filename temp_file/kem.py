from pymongo import MongoClient

class KemMongoCache(object):
    def __init__(self, uri = 'mongodb://140.120.13.243:4444/'):
        self.client = MongoClient(uri)
        self.db = self.client['database']
        self.coll = self.db['kem_test_coll']


    def queryTerm():
      result = self.coll.find()






    def main(self):
        # testData = {'name':'Eating', 'age':'13'}
        # result = self.coll.insert(testData)
        # print(result)





if __name__ == '__main__':
    obj = KemMongoCache()
    obj.main()