from pymongo import MongoClient

class KemMongoCache(object):
    def __init__(self, uri = 'mongodb://140.120.13.243:4444/'):
        self.client = MongoClient(uri)
        self.db = slef.client['database']
        self.coll = self.db['dataset']

    def main(self):




if __name__ == '__main__':
    obj = KemMongoCache()
    obj.main()