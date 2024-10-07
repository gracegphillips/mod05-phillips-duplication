from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/animals')
def animals():
    return render_template('animals.html')


