from flask import Flask , render_template , request
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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/users')
def users():
    return {
        "data":[
            {"id":"1", "Lietotaja vards":"Maris007", "Vards":"Maris", "Uzvards":"Danne", "Personas kods":"11111-11111", "Parole":"maris123", "E-pasts":"maritis@inbox.lv", "Talrunis":"27722195"},
            {"id":"2", "Lietotaja vards":"Aligators2", "Vards":"Dainis", "Uzvārds":"Berzins", "Personas kods":"020500-203948", "Parole":"NavigatorsAligators", "E-pasts":"Aligators@inbox.lv", "Talrunis":"27948374"},
        ]

    }

@app.route('/user/<id>')
def user(id):
    if id == "1":
        return {"id":"1", "Lietotaja vards":"Maris007", "Vards":"Maris", "Uzvards":"Danne", "Personas kods":"11111-11111", "Parole":"maris123", "E-pasts":"maritis@inbox.lv", "Talrunis":"nr", "status":"admin"}
    elif id == "2":
        return {"id":"2", "Lietotaja vards":"Aligators2", "Vards":"Dainis", "Uzvārds":"Berzins", "Personas kods":"020500-203948", "Parole":"NavigatorsAligators", "E-pasts":"Aligators@inbox.lv", "Talrunis":"nr", "status":"user"}
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