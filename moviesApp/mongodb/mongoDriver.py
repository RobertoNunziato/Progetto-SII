import sys
sys.path.append("/anaconda/bin/python2.7/site-packages")
from pymongo import MongoClient
from bson.json_util import dumps
from helpers import helpers
from model.user import User

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

    return userLogged

def verifyUser(email):
    if db.users.find({'email':email}).count() == 1:
        return True
    return False