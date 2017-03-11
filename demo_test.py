# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import json

def main():
    print('Loading model...')
    model = models.KeyedVectors.load_word2vec_format('med250.model.bin',binary=True)
    # models.KeyedVectors.load_word2vec_format

    try:
        print('Running most_similar function')

        res = model.most_similar('中興大學',topn = 100)
        print("中興大學相似詞前 100 排序")
        print(type(res))
        # for item in res:
            # print(item[0]+","+str(item[1]))
            # print(item)
            # break
        # with open('w2v_result.json', 'w') as f:
        #     json.dump(res, f)

    except Exception as e:
        print(repr(e))

if __name__ == "__main__":
    main()
