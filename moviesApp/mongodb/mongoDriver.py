import sys
sys.path.append("/anaconda/bin/python2.7/site-packages")
from pymongo import MongoClient
from bson.json_util import dumps
from helpers import helpers

client = MongoClient()
db = client.movielens

def getFilm():
    return dumps(db.movies.find({'movieId':19}))

def insertUser(user,preferences):
    name = (user['name'])
    surname = (user['surname'])
    email = (user['email'])
    password = (user['password'])
    age = (user['age'])
    gender = (user['gender'])
    profession = (user['profession'])
    education = (user['education'])
    preferences = helpers.buildPreferences(preferences)

    user = {'name':name,'surname':surname,'email':email,'password':password,'age':age,
            'gender':gender,'profession':profession,'education':education,'preferences':preferences}

    db.users.insert_one(user)

def getUser(form):
    email = form['email']
    password = form['login']

    if db.users.find({'$and':[{'email':email},{'password':password}]}).count() == 1:
        return True
    else:
        return False

def verifyUser(email):
    print email
    if db.users.find({'email':email}).count() == 1:
        return True
    return False