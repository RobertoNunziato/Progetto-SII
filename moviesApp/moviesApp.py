from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    #pagina html con interazione con mongo e' index.html
    return render_template('homepage.html')

@app.route('/getRegistrationModule/',methods=['POST'])
def getRegitrationModule():
    return render_template('homepage.html',registration=True)

@app.route('/registration/',methods=['POST'])
def registration():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    password = request.form['password']
    print name," ",surname," ",email," ",password
    return redirect(url_for('index'))

""" Funzionano
@app.route('/cercaFilm/')
def cercaFilm():
    data = request.args.get('nomeFilm')
    print data
    return mongoDriver.getFilm()

@app.route('/login/', methods=['POST'])
def login():
    filmName = request.form['filmName']
    print filmName

    return redirect(url_for('index',filmName=filmName))
"""

#App start on localhost:5000
if __name__ == '__main__':
    app.run()
