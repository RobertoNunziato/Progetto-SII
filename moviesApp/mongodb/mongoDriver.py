import sys
sys.path.append("/anaconda/bin/python2.7/site-packages")
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
db = client.movielens

def getFilm():
    return dumps(db.movies.find({'movieId':19}))
