import sys
sys.path.append("/anaconda/bin/python2.7/site-packages")
from pymongo import MongoClient
from model.user import User


client = MongoClient()
db = client.movielens

def updateUser(user):
    db.users.delete_many({"email": user['email']})
    user = {'name': user['name'], 'surname': user['surname'], 'email': user['email'], 'password': user['password'], 'age': user['age'],
            'gender': user['gender'], 'profession': user['profession'], 'education': user['education'], 'preferences': user['preferences'],
            'personality':user['personality']}
    db.users.insert_one(user)

    updatedUser = User(user['name'],user['surname'],user['email'],user['password'],
                      user['age'],user['gender'],user['profession'],user['education'])
    updatedUser.setPreferences(user['preferences'])
    updatedUser.setPersonality(user['personality'])
    return updatedUser

def insertUser(user,preferences):
    name = (user['name'])
    surname = (user['surname'])
    email = (user['email'])
    password = (user['password'])
    age = (user['age'])
    gender = (user['gender'])
    profession = (user['profession'])
    education = (user['education'])
    personality = (user['personality'])
    if len(preferences) >= 17:
        user['preferences'] = []
        user = {'name': name, 'surname': surname, 'email': email, 'password': password, 'age': age,
                'gender': gender, 'profession': profession, 'education': education, 'preferences': [], 'personality':personality}

    else:
        user['preferences'] = preferences
        user = {'name': name, 'surname': surname, 'email': email, 'password': password, 'age': age,
            'gender': gender, 'profession': profession, 'education': education, 'preferences': preferences, 'personality':personality}

    db.users.insert_one(user)


def getUser(form):
    email = form['email']
    email = email.strip()
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
        print("GETUSER---->",(user[0]['personality']))
        userLogged.setPersonality(user[0]['personality'])

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
    else:
        for i in range(10):
            result.append(films[i])

    return result

def getFilmBestRatedByGenre(genre):
    result=[]

    films = db.movies.aggregate([ {'$match': {'genres': {'$regex': genre, '$options': 'i'}}}, {'$sample': {'size':2}} ])
    for film in list(films):
        result.append(film)

    return result


def getLink(id):
    movie = db.links.find({'movieId':id})
    return movie[0]['tmdbId']

def getIdMovielens(codeTmdb):
    codeTmdb=long(codeTmdb)
    movie = db.links.find({'tmdbId':codeTmdb})
    if movie.count()==0:
        return 0
    id=movie[0]['movieId']
    return id

def getRandomFilmsByGenre(preferences):
    films = []

    if len(preferences)==5:
        size = 3
    elif len(preferences)>=6 and len(preferences)<=8:
        size = 2
    elif len(preferences)>=9:
        size = 1


    for preference in preferences:
        result = db.movies.aggregate([ {'$match': {'genres': {'$regex': preference, '$options': 'i'}}}, {'$sample': {'size':size}} ])
        for film in list(result):
            films.append(film)

    return films


def insertFilmRatings(user,ratings):
    for elem in ratings:
        for filmId in elem:
            json = {'email':user['email'],'filmId':int(filmId),'rating':int(elem[filmId])}
            db.usersRatings.insert_one(json)


def rateSingleFilm(rating,filmId,user):
    print(filmId)
    if db.usersRatings.find({'$and':[{'filmId':int(filmId)},{'email':user['email']}]}).count()>0:
        db.usersRatings.delete_many({'$and':[{'filmId':int(filmId)},{'email':user['email']}]})

    json = {'email':user['email'],'filmId':int(filmId),'rating':int(rating)}
    db.usersRatings.insert_one(json)

def checkRating(user,filmId):
    if db.usersRatings.find({'$and': [{'filmId': int(filmId)}, {'email': user['email']}]}).count() > 0:
        result = db.usersRatings.find({'$and': [{'filmId': int(filmId)}, {'email': user['email']}]})
        return result[0]['rating']
    return None

def getTitleAndGenresFilm(filmId):
    movie = db.movies.find({'movieId':filmId})
    return [movie[0]['title'],movie[0]['genres']]

#userMovies(session['user'])
def userMovies(user):
    ratingFilms = db.usersRatings.find({'email':user['email']})
    data=[]
    for film in list(ratingFilms):
        id= film['filmId']
        title = getTitleAndGenresFilm(id)[0]
        genres = getTitleAndGenresFilm(id)[1]
        rating=film['rating']
        data.append([id,title,genres,rating])
    return data



def usersBestMovies(user,numberTop):
    result = db.usersRatings.aggregate([{'$match':{'$and':[{'email': user['email']},{'rating':{'$gte':3}}]}},{'$sample': {'size':numberTop}}])
    movies=[]
    for film in list(result):
        id= film['filmId']
        movies.append(getLink(id))
    return movies



"""
Query fondamentale:
-Per prendere N film random dato un genere:
    db.movies.aggregate([ {$match: {genres: {'$regex': 'drama', '$options': 'i'}}}, {$sample: {size:10}} ])

"""
