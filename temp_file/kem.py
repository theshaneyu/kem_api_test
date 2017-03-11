import pprint
import json
from gensim import models
from gensim.models import word2vec


class KemMongoCache(object):
    def __init__(self, uri = 'mongodb://140.120.13.243:4444/'):
        from pymongo import MongoClient
        self.client = MongoClient(uri)
        self.db = self.client['database']
        self.coll = self.db['kem_test_coll']
        self.model = models.KeyedVectors.load_word2vec_format('med250.model.bin',binary=True)


    def testQueryTerm(self):
        for item in self.coll.find():
            print(item)


    def testInsert(self):
        testData = {'name':'Eating', 'age':'13'}
        result = self.coll.insert(testData)
        print(result)


    def resultToJson(self):
        # print('Loading model...')
        # model = models.KeyedVectors.load_word2vec_format('med250.model.bin',binary=True)

        try:
            print('Running most_similar function')

            res = self.model.most_similar('中興大學',topn = 100)
            print("中興大學相似詞前 100 排序")
            # print(res)
            # for item in res:
                # print(item[0]+","+str(item[1]))
                # print(item)
                # break
            resJson = json.dump(res)
            print(resJson)

        except Exception as e:
            print(repr(e))



    def main(self):
        # self.queryTerm()
        self.resultToJson()





if __name__ == '__main__':
    obj = KemMongoCache()
    obj.main()