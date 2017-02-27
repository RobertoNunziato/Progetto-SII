from __future__ import print_function
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, json
from mongodb import mongoDriver
from model.user import User
from helpers import helpers
import json
from filmDataExtraction import getDataMovie


app = Flask(__name__)
cont = 1
survey = {"1":[0,0,0,0,0,0,0,0,0,0],
          "2":[0,0,0,0,0,0,0,0,0,0],
          "3":[0,0,0,0,0,0,0,0,0,0],
          "4":[0,0,0,0,0,0,0,0,0,0],
          "5":[0,0,0,0,0,0,0,0,0,0]}

@app.route('/')
def index():
    if (session):
        del session['user']

    print (session)
    return render_template('homepage.html')

@app.route('/getRegistrationModule/',methods=['POST'])
def getRegitrationModule():
    return render_template('homepage.html',registration=True)

@app.route('/registration/',methods=['POST'])
def registration():
    user = User(request.form['name'],request.form['surname'],request.form['email'],request.form['password'],
                request.form['age'],request.form['gender'],request.form['profession'],request.form['education'])

    session['user'] = user.serialize()
    session['survey'] = json.dumps(helpers.reformat(survey))
    return render_template('survey.html',page=cont,survey=survey)

@app.route('/login/',methods=['POST'])
def login():
    user = mongoDriver.getUser(request.form)
    if user != None:
        filmSuggested = mongoDriver.getRandomFilmsByGenre((user.getPreferences()))
        print ("FILM SUGGESTED[SERVER]",filmSuggested)
        session['user'] = user.serialize()
        return render_template('homepageUtente.html')
    else:
        return render_template("homepage.html",user=None)

@app.route('/logout/')
def logout():
    del session['user']
    return render_template("homepage.html")

@app.route('/completeRegistration/', methods=['POST'])
def completeRegistration():
    global survey
    preferences = request.form['preferences']
    user = session['user']

    preferences = helpers.buildPreferences(preferences)

    mongoDriver.insertUser(user,preferences)
    print (user)
    #clean survey
    survey = {"1": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              "2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              "3": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              "4": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              "5": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    del session['survey']


    #If there're more than 5 preferences(case of ambiguous personality),
    #redirect to page in which user can choice 5 genres
    if len(preferences) == 17:
        preferences = []
    if len(preferences) < 5 or len(preferences) >= 17:
        return render_template("chooseFilmsGenres.html",number=len(preferences),pref=preferences)
    else:
        films = mongoDriver.getRandomFilmsByGenre(preferences)
        return render_template("rateFilms.html",films=films)

@app.route('/getSurveyPage/',methods=['POST'])
def getSurveyPage():
    global cont
    cont = int(request.form['number'])
    choices = request.form['choices']
    pageNumber = choices.split(":")[0]
    answers = choices.split(":")[1]
    answersArray = answers.split(",")
    survey[pageNumber] = answersArray

    session['survey'] = json.dumps(helpers.reformat(survey))
    """Prove sessione"""
    #user = session['user']
    #(print(user['name']))
    return render_template("survey.html",page=cont,survey=survey)

@app.route('/verifyUser/')
def verifyUser():
    email = request.args.get('email')
    return jsonify(mongoDriver.verifyUser(email))

@app.route('/userPage/')
def getUserPage():
    return render_template("user.html")

@app.route('/movie/', methods=['POST'])
def getMovie():
    id=request.form['movieid']
    movieId = mongoDriver.getLink(long(id))
    movieData = getDataMovie.getDataFilm(movieId)
    return render_template("movie.html",movieData=movieData)

@app.route('/homeUtente/')
def userHome():
    if(session['user'] != None):
        print ("SESSION ---> ",(session['user']))

    filmSuggested = mongoDriver.getRandomFilmsByGenre(session['user']['preferences'])
    print("FILM SUGGESTED[SERVER]", filmSuggested)
    return render_template("homepageUtente.html")

@app.route('/searchFilm/', methods=['POST'])
def searchFilm():
    search = request.form['search']
    films = mongoDriver.searchFilm(search)
    return render_template("listaFilm.html",films=films)

@app.route('/rateFilm/<rating>')
def rateFilm(rating):
    print (rating)
    return render_template("movie.html")


@app.route('/updateFilmsPreferences/', methods=['POST'])
def updateFilmPreferences():
    print(session['user'])
    preferences = request.form['preferences']
    newPreferences = helpers.buildPreferences(preferences)
    oldPreferences = (session['user']['preferences'])

    #Fai merge delle liste..
    if(len(newPreferences)+len(oldPreferences)) == 5:
        oldPreferences = helpers.buildPreferences((session['user']['preferences']))
        for list in oldPreferences:
            for preference in list:
                newPreferences.append(preference)
    (session['user']['preferences']) = newPreferences   #Funzionamento strano, rimedio creando utente da capo
    print(session['user'])
    #Update user with new preferences...
    updatedUser = mongoDriver.updateUser(session['user'])
    del session['user'] #Cancello il vecchio utente dalla sessione
    session['user'] = updatedUser.serialize()

    films = mongoDriver.getRandomFilmsByGenre(newPreferences)

    return render_template("rateFilms.html",films=films)

#App start on localhost:5000
if __name__ == '__main__':
    app.secret_key = 'RENOMIBACENORULTEAOLE'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()
