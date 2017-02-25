import sys
sys.path.append("/anaconda/bin/python2.7/site-packages")
from pymongo import MongoClient
from bson.json_util import dumps
from helpers import helpers
from model.user import User
import json

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
    user['preferences']=preferences


    user = {'name':name,'surname':surname,'email':email,'password':password,'age':age,
            'gender':gender,'profession':profession,'education':education,'preferences':preferences}

    db.users.insert_one(user)


def getUser(form):
    email = form['email']
    password = form['password']
    user = db.users.find({'$and':[{'email':email},{'password':password}]})
    userLogged = None

    if db.users.find({'$and':[{'email':email},{'password':password}]}).count() > 0:
        preferences = []
        userLogged = User(user[0]['name'], user[0]['surname'], user[0]['email'], user[0]['password'],
                    user[0]['age'], user[0]['gender'], user[0]['profession'], user[0]['education'])
        for preference in user[0]['preferences']:
            preferences.append(preference)
        userLogged.setPreferences(preferences)

    return userLogged

def verifyUser(email):
    if db.users.find({'email':email}).count() == 1:
        return True
    return False

def searchFilm(search):
    result=[]
    numbers = db.movies.find({'title': {'$regex': search, '$options': 'i'}}).count()
    films = db.movies.find({'title': {'$regex': search, '$options': 'i'}}).limit(10)
    if numbers == 1:
        result.append(films[0])
        return result

    elif numbers <= 10:
        for i in range(numbers):
            result.append(films[i])

    return result