from pymongo import MongoClient
import pprint


class KemMongoCache(object):
    def __init__(self, uri = 'mongodb://140.120.13.243:4444/'):
        self.client = MongoClient(uri)
        self.db = self.client['database']
        self.coll = self.db['kem_test_coll']


    def queryTerm(self):
        for item in self.coll.find():
            print(item)





    def main(self):
        # testData = {'name':'Eating', 'age':'13'}
        # result = self.coll.insert(testData)
        # print(result)
        self.queryTerm()





if __name__ == '__main__':
    obj = KemMongoCache()
    obj.main()