from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId


client = MongoClient("mongodb+srv://niks:BgizhM1Zh1HYAgw1@dp23-5grupa-medicina.1bqly.mongodb.net/medicina?retryWrites=true&w=majority")
db = client.medicina

# tabulas / dokumenti
users_db = db.users

# user1 = {"Lietotaja vards":"Maris007", "Vards":"Maris", "Uzvards":"Danne", "Personas kods":"11111-11111", "Parole":"maris123", "E-pasts":"maritis@inbox.lv", "Talrunis":"27722195", "status":"admin"}
# users_db.insert_one(user1)
# exit()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Aktualitātes.html')

@app.route('/slimnicas')
def slimnicas():
    return render_template('slimnicas.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods = ["POST"])
def checklogin():
    loginVards = request.form['loginVards']
    loginParole = request.form['loginParole']

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

@app.route('/vizites')
def vizites():
    return render_template('vizites.html')

@app.route('/pieteiktviz')
def pieteiktviz():
    return render_template('pieteiktviz.html')

@app.route('/manasviz')
def manasviz():
    return render_template('manasviz.html')

@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')

@app.route('/adminPanel2')
def adminPanel2():
    return render_template('adminPanel2.html')

@app.route('/adminPanelSlimnicas')
def adminPanelSlimnicas():
    return render_template('adminPanelSlimnicas.html')
    
app.run(host="0.0.0.0", port=80, debug=True)