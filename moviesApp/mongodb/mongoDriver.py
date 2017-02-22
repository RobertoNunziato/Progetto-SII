import sys
sys.path.append("/anaconda/bin/python2.7/site-packages")
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
db = client.movielens

def getFilm():
    return dumps(db.movies.find({'movieId':19}))

def insertUser(form):
    name = form['name']
    surname = form['surname']
    email = form['email']
    password = form['password']
    age = form['age']
    gender = form['gender']
    profession = form['profession']
    education = form['education']

    user = {'name':name,'surname':surname,'email':email,'password':password,'age':age,
            'gender':gender,'profession':profession,'education':education}

    db.users.insert_one(user)
