from flask import Flask, render_template, request, json, jsonify, redirect, session, url_for

from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = b'\xf0\x14\x9a'

client = MongoClient("mongodb+srv://niks:BgizhM1Zh1HYAgw1@dp23-5grupa-medicina.1bqly.mongodb.net/medicina?retryWrites=true&w=majority")
db = client.medicina

# tabulas / dokumenti
users_db = db.users

# user1 = {"Lietotaja vards":"Maris007", "Vards":"Maris", "Uzvards":"Danne", "Personas kods":"11111-11111", "Parole":"maris123", "E-pasts":"maritis@inbox.lv", "Talrunis":"27722195", "status":"admin"}
# users_db.insert_one(user1)
# exit()

@app.route('/')
def home():
    if 'user' in session:
        if session['user'] == 'admin@gmail.com':
            return render_template('Aktualitātes.html', data = db.test.find(), status = 'admin')
    return render_template('Aktualitātes.html', data = db.test.find(), status = None)

@app.route('/slimnicas')
def slimnicas():
    if 'user' in session:
        if session['user'] == 'admin@gmail.com':
            return render_template('slimnicas.html', data = db.test.find(), status = 'admin')
    return render_template('slimnicas.html', data = db.test.find(), status = None)

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':

        if request.form.get('login') == 'admin@gmail.com' and request.form.get('password') == 'admin':
            session['user'] = request.form.get('login')
            return redirect('/')


    else:
        if 'user' in session:
            return redirect('/')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/users')
def users():
    users_data = users_db.find()
    if users_data:
        return dumps(users_data)
    else:
        return {"error":"No users in DB"}

    return "1"

@app.route('/user/create', methods = ['POST'])
def createUser():
    if request.method == 'POST' and request.content_type == 'application/json':    
        dati = request.json
        users_db.insert_one({"vards":dati['vards'], "uzvards":dati['uzvards'], "status":dati['status']})
        return {"messange":"User created!"}
    else:
        return {"error":"Method or content type not supported!"}

@app.route('/user/<id>')
def user(id):
    user = users_db.find_one({"_id":ObjectId(id)})
    if user:
        return dumps(user)
    else:
        return {"error":"User not found!"}

@app.route('/pieteiktviz')
def pieteiktviz():
    if 'user' in session:
        if session['user'] == 'admin@gmail.com':
            return render_template('pieteiktviz.html', data = db.test.find(), status = 'admin')
    return render_template('pieteiktviz.html', data = db.test.find(), status = None)

@app.route('/manasviz')
def manasviz():
    if 'user' in session:
        if session['user'] == 'admin@gmail.com':
            return render_template('manasviz.html', data = db.test.find(), status = 'admin')
    return render_template('manasviz.html', data = db.test.find(), status = None)

@app.route('/kontakti')
def kontakti():
    if 'user' in session:
        if session['user'] == 'admin@gmail.com':
            return render_template('kontakti.html', data = db.test.find(), status = 'admin')
    return render_template('kontakti.html', data = db.test.find(), status = None)

@app.route('/adminPanel2')
def adminPanel2():
    if 'user' in session:
        if session['user'] == 'admin@gmail.com':
            return render_template('adminPanel2.html', data = db.test.find(), status = 'admin')
    return render_template('adminPanel2.html', data = db.test.find(), status = None)

@app.route('/adminPanelSlimnicas')
def adminPanelSlimnicas():
    if 'user' in session:
        if session['user'] == 'admin@gmail.com':
            return render_template('adminPanelSlimnicas.html', data = db.test.find(), status = 'admin')
    return render_template('adminPanelSlimnicas.html', data = db.test.find(), status = None)
    
app.run(host="0.0.0.0", port=80, debug=True)