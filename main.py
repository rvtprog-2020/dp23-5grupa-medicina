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

app.run(host="0.0.0.0", port=80, debug=True)