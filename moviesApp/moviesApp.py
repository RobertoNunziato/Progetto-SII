from __future__ import print_function
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from mongodb import mongoDriver
from model.user import User

app = Flask(__name__)
cont = 1
survey = {'1':[0,0,0,0,0,0,0,0,0,0],
          '2':[0,0,0,0,0,0,0,0,0,0],
          '3':[0,0,0,0,0,0,0,0,0,0],
          '4':[0,0,0,0,0,0,0,0,0,0],
          '5':[0,0,0,0,0,0,0,0,0,0]}

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/getRegistrationModule/',methods=['POST'])
def getRegitrationModule():
    return render_template('homepage.html',registration=True)

@app.route('/registration/',methods=['POST'])
def registration():
    user = User(request.form['name'],request.form['surname'],request.form['email'],request.form['password'],
                request.form['age'],request.form['gender'],request.form['profession'],request.form['education'])

    session['user'] = user.serialize()

    #mongoDriver.insertUser(request.form)
#    return render_template('survey.html',user=user,page=cont,survey=survey)
    return render_template('survey.html',page=cont,survey=survey)

@app.route('/login/',methods=['POST'])
def login():
    if mongoDriver.getUser(request.form):
        return render_template('homepage.html',user=request.form)
    else:
        return render_template("homepage.html",user=None)


@app.route('/completeRegistration/', methods=['POST'])
def completeRegistration():
    return render_template("homepage.html")

@app.route('/getSurveyPage/',methods=['POST'])
def getSurveyPage():
    global cont
    cont = int(request.form['number'])
    choices = request.form['choices']
    pageNumber = choices.split(":")[0]
    answers = choices.split(":")[1]
    answersArray = answers.split(",")
    survey[pageNumber] = answersArray


    """Prove sessione"""
    user = session['user']

    (print(user['name']))



#    return render_template("survey.html",page=cont,survey=survey,user=user)
    return render_template("survey.html",page=cont,survey=survey)

@app.route('/userPage/')
def getUserPage():
    return render_template("user.html")


#App start on localhost:5000
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()
