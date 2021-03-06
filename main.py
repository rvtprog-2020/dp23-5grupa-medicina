from flask import Flask, render_template, request, json, jsonify, redirect, session, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import bcrypt
import pymongo

app = Flask(__name__)

app.secret_key = b'\xf0\x14\x9a'

client = MongoClient("mongodb+srv://niks:BgizhM1Zh1HYAgw1@dp23-5grupa-medicina.1bqly.mongodb.net/medicina?retryWrites=true&w=majority")
db = client.medicina

# tabulas / dokumenti
users_db = db.users
info_db = db.info
add_db = db.add
arsts_db = db.arsts
# info1 = {"time":"9:00","date":"Otrdiena","job":"Psihologs","hospital":"Rīgas Austrumu slimnīca","doctor":"Valters Upenieks"}
# info_db.insert_one(info1)
# exit()
# user1 = {"Lietotaja vards":"Maris007", "Vards":"Maris", "Uzvards":"Danne", "Personas kods":"11111-11111", "Parole":"maris123", "E-pasts":"maritis@inbox.lv", "Talrunis":"27722195", "status":"admin"}
# users_db.insert_one(user1)
# exit()

@app.route('/arsti')
def arsti():
    if 'username' in session:
        if session['username'] == 'admin':
            return render_template('arsti.html',username=session['username'], status = 'admin')
        return render_template('arsti.html',username=session['username'], status = 'user')
    return render_template('loginpage.html')

@app.route('/arsti2', methods = ['GET','POST'])
def arsti2():
    arsts_data = arsts_db.find()
    if arsts_data:
        return dumps(arsts_data)
    else:
        return {"error":"No users in DB"}
    return "1"

@app.route('/arstia', methods = ['GET','POST'])
def arstiAdd():
    if request.method == 'POST':
        dati = request.json
        arsts_db.insert_one({"name":dati['arstavards'],"surname":dati['arstauzvards'],"hospital":dati['hospital'],"job":dati['Specaialty']}) #Ārsta laiks nav pievienots!
        return {"message":"Arsts pievienots!"}
    else:
        return{"Error":"Arsts nav pievienots!"}

@app.route('/add', methods = ['POST'])	
def add(id):	
    if request.method == 'POST':	
        dati = request.json	
        add_db.insert_one({"name":dati['name'], "location":dati['location'], "start":dati['start'], "end":dati['end']})	
        return {"messange":"New hospital created!"}	
    else:
        return {"error":"Method or content type not supported!"} 

@app.route('/edit/<string:id>', methods = ['POST'])	
def edit(id):	
    if request.method == 'POST':	
        dati = request.json	
        add_db.update(add_db.find_one(ObjectId(id)), {"name":dati['name'], "location":dati['location'], "start":dati['start'], "end":dati['end']})
        return {"messange":"New hospital created!"}	
    else:
        return {"error":"Method or content type not supported!"}
@app.route('/adds', methods = ['GET'])
def GetADD():
    add_data = add_db.find()
    if add_data:
        return dumps(add_data)
    else:
        return {"error":"No hospital in DB"}
@app.route('/adds/<string:id>', methods = ['GET'])
def addID(id):
    add_data = add_db.find_one(ObjectId(id))
    if add_data:
        return dumps(add_data)
    else:
        return {"error":"No hospital in DB"}

@app.route('/info/print/<id>', methods = ['GET','POST']) #Drukāt nav pabeigts!
def printId(id):
    info = info_db.find({"_id":ObjectId(id)})
    if info:
        return dumps(info)
    else:
        return {"message":"Šāda vizīte nepastāv!"}

@app.route('/info/delete/<id>', methods = ['GET','POST'])
def infoDelete(id):
    dati = request.json
    info = info_db.find_one_and_delete({"time":dati['time'], "date":dati['date'], "job":dati['job'], "hospital":dati['hospital'], "doctor":dati['doctor']})
    if info:
        return{"message":"Vizīte izdzēsta!"}
    else:
        return {"message":"Vizīte netika izdzēsta!"}

@app.route('/infos', methods = ['GET','POST']) #Ķļūda dēl Ārstiem!
def infos():
    info_data = info_db.find()
    if info_data:
        return dumps(info_data)
    else:
        return {"error":"No users in DB"}
    return "1"

@app.route('/info', methods = ['GET','POST'])	
def info():	
    if request.method == 'POST':	
        dati = request.json	
        info_db.insert_one({"time":dati['time'], "date":dati['date'], "job":dati['job'], "hospital":dati['hospital'], "doctor":dati['doctor']})	
        return {"messange":"New info created!"}	
    else:
        info_db.find_one()
        return {"error":"Method or content type not supported!"} 

@app.route('/info/<id>')
def infos2(id):
    info = info_db.find_one({"_id":ObjectId(id)})
    if info:
        return dumps(info)
    else:
        return {"error":"User not found!"}
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
    login_user = users.find_one({'username': request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            session['status'] = 1
            return redirect(url_for('home'))
    return render_template('loginpage.html', error = 'Nepareizs lietotājvārds vai parole!')

@app.route('/logout')
def logout():
	session.pop('username', None), session.pop('status', None)
	return redirect('/') 
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name':request.form['name'], 'surname':request.form['surname'], 'username':request.form['username'], 'email':request.form['email'], 'password': hashpass, 'personalcode':request.form['per1'] +'-'+ request.form['per2'], 'telephone':request.form['tel']})
            session['username'] =  request.form['username']
            session['status'] = 1
            return redirect(url_for('home'))
        error = "That username already exists!"
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

@app.route('/manasviz', methods=['GET','POST'])
def manasviz():
    info_data = info_db.find()
    if info_data:
        print('Dati iegūti')
    else:
        return {"error":"No info in DB"}
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

@app.route('/users')
def users():
    users_data = db.users.find()
    if users_data:
        return dumps(users_data)
    else:
        return {"error":"No users in DB"}

    return "1"

@app.route('/user/<id>')
def user(id):
    user = db.users.find_one({"_id":ObjectId(id)})
    if user:
        return dumps(user)
    else:
        return {"error":"User not found!"}

@app.route('/user/create', methods = ['POST'])
def createUser():
    if request.method == 'POST' and request.content_type == 'application/json':    
        dati = request.json
        db.users.find_one({"vards":dati['vards'], "uzvards":dati['uzvards'], "status":dati['status']})
        return {"messange":"User created!"}
    else:
        return {"error":"Method or content type not supported!"}




### TEST

# @app.route('/arsti')
# def test():
#     if session['username'] == 'admin':
#         return render_template('arsti.html',username=session['name'], data = db.users.find(), status = 'admin')
#     return render_template('arsti.html',username=session['name'], data = db.users.find(), status = 'admin')


# @app.route('/arsts', methods = ['GET','POST'])
# def arsts():
#     arsts_data = db.arsts.find()
#     if arsts_data:
#         return dumps(arsts_data)
        
# @app.route('/arsts')
# def arsts():
#     db.userdetails.insert({"name" : 'Niks',"surname" : "Veidemanis"})    
# @app.route('/arsti')
# def arsti():

#     mydb = client['medicina']
#     mycol = mydb['arsts']
#     name = db.arsts.find_one({"name" : "Niks"})
#     for x in mycol.find():
#         return render_template('arsti.html', name=name)
#     print('Done')



app.run(host="0.0.0.0", port=8080, debug=True)