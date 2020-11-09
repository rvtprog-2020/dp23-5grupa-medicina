from flask import Flask , render_template , request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Aktualitātes.html')

@app.route('/login')
def login():
    return render_template('login.html')
app.run(host="0.0.0.0", port=300, debug=True)