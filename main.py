from flask import Flask, render_template, request, json, jsonify, redirect, session, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.secret_key = b'\xf0\x14\x9a'

client = MongoClient("mongodb+srv://niks:BgizhM1Zh1HYAgw1@dp23-5grupa-medicina.1bqly.mongodb.net/medicina?retryWrites=true&w=majority")
db = client.medicina

@app.route('/info', methods = ['POST'])	
def info():	
    if request.method == 'POST':	
        dati = request.json	
        info_db.insert_one({"time":dati['time'], "date":dati['date'], "job":dati['job'], "hospital":dati['hospital']})	
        return {"messange":"New info created!"}	
    else:	
        return {"error":"Method or content type not supported!"} 

@app.route('/')
def home():
    if 'username' in session:
        if session['username'] == 'admin':
            return render_template("aktualitātes.html", username=session['username'], data = db.users.find(), status = 'admin')
        return render_template('aktualitātes.html', username=session['username'], data = db.users.find(), status = 'user')
    else:
        return render_template('loginpage.html')

@app.route('/login', methods=['POST'])
def login():
    users = db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect('/')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name':request.form['username'], 'password': hashpass})
            session['username'] =  request.form['username']
            return redirect(url_for('home'))

        return 'That username already exists!'

    return render_template('register.html')

#### Slimnicas

@app.route('/slimnicas')
def slimnicas():
    if 'username' in session:
        if session['username'] == 'admin':
            return render_template('slimnicas.html',username=session['username'], data = db.users.find(), status = 'admin')
        return render_template('slimnicas.html',username=session['username'], data = db.users.find(), status = 'user')
    return render_template('loginpage.html')


#### Vizītes

@app.route('/pieteiktviz', methods=['GET','POST'])
def pieteiktviz():
    if 'user' in session:
        if session['user'] == 'admin':
            return render_template('pieteiktviz.html',username=session['username'], data = db.users.find(), status = 'admin')
    return render_template('pieteiktviz.html',username=session['username'], data = db.users.find(), status = 'user')

@app.route('/manasviz')
def manasviz():
    if 'user' in session:
        if session['user'] == 'admin':
            return render_template('manasviz.html',username=session['username'], data = db.users.find(), status = 'admin')
    return render_template('manasviz.html',username=session['username'], data = db.users.find(), status = 'user')

#### Kontakti

@app.route('/kontakti')
def kontakti():
    if 'username' in session:
        if session['username'] == 'admin':
            return render_template('kontakti.html',username=session['username'], data = db.users.find(), status = 'admin')
        return render_template('kontakti.html',username=session['username'], data = db.users.find(), status = 'user')
    return render_template('kontakti.html')

#### Admin

@app.route('/adminPanel2')
def adminPanel2():
    if session['username'] == 'admin':
        return render_template('adminpanel2.html',username=session['username'], data = db.users.find(), status = 'admin')
    return 'Tu neesi admins!'

@app.route('/adminPanelSlimnicas')
def adminPanelSlimnicas():
    if session['username'] == 'admin':
        return render_template('adminpanelslimnicas.html',username=session['username'], data = db.users.find(), status = 'admin')
    return 'Tu neesi admins!'

#### Skolotāja kods ####

# @app.route('/users')
# def users():
#     users_data = users_db.find()
#     if users_data:
#         return dumps(users_data)
#     else:
#         return {"error":"No users in DB"}

#     return "1"

# @app.route('/user/<id>')
# def user(id):
#     user = users_db.find_one({"_id":ObjectId(id)})
#     if user:
#         return dumps(user)
#     else:
#         return {"error":"User not found!"}

# @app.route('/user/create', methods = ['POST'])
# def createUser():
#     if request.method == 'POST' and request.content_type == 'application/json':    
#         dati = request.json
#         users_db.insert_one({"vards":dati['vards'], "uzvards":dati['uzvards'], "status":dati['status']})
#         return {"messange":"User created!"}
#     else:
#         return {"error":"Method or content type not supported!"}

    
app.run(host="0.0.0.0", port=80, debug=True)