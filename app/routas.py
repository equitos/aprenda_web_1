from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

