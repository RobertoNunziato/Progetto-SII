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
    return redirect(url_for('index'))


#App start on localhost:5000
if __name__ == '__main__':
    app.run()
