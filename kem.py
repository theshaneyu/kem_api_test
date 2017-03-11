import json


class KemMongoCache(object):
    def __init__(self, uri):
        from gensim import models
        from pymongo import MongoClient
        self.client = MongoClient(uri)
        self.db = self.client['database']
        self.coll = self.db['kem_test_coll']
        self.model = models.KeyedVectors.load_word2vec_format('med250.model.bin',binary=True)


    def getTerms(self, query, num):
        result = self.coll.find({'Term':query}, {'Result':1, '_id':False}).limit(1)
        if result.count() == 0:
            resultJson = self.getJsonResult(query, num)
            self.insertMongo(query, resultJson)
            return resultJson

        return (list(result)[0])['Result']

        # print(type(result)) # <class 'pymongo.cursor.Cursor'>
        # print((list(result)[0])['Result'])


    def insertMongo(self, queryTerm, resultList):
        state = self.coll.insert({'Term':queryTerm, 'Result':resultList})
        print(state)



    def getJsonResult(self, queryStr, number):
        from gensim.models import word2vec
        try:
            print('Running most_similar function')

            res = self.model.most_similar(queryStr, topn = number) # most_similar return a list
            print(queryStr + '相似詞前' + str(number) + '排序')
            resJson = json.dumps(res)

            return resJson

        except Exception as e:
            print(repr(e))


    def main(self):
        # self.queryTerm()
        testInput = '日本'
        # jsonResult = self.getJsonResult(testInput)
        # self.insertMongo(testInput, jsonResult)
        temp = self.getTerms(testInput, 100)
        print(type(temp))



if __name__ == '__main__':
    obj = KemMongoCache('mongodb://140.120.13.243:4444/')
    obj.main()
