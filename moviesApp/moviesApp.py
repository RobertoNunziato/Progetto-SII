from flask import Flask, render_template, request, redirect, url_for
from mongodb import mongoDriver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/getRegistrationModule/',methods=['POST'])
def getRegitrationModule():
    return render_template('homepage.html',registration=True)

@app.route('/registration/',methods=['POST'])
def registration():
    #mongoDriver.insertUser(request.form)
    return render_template('survey.html',user=request.form)

@app.route('/login/',methods=['POST'])
def login():
    if mongoDriver.getUser(request.form):
        return render_template('homepage.html',user=request.form)
    else:
        return render_template("homepage.html",user=None)

#App start on localhost:5000
if __name__ == '__main__':
    app.run()
