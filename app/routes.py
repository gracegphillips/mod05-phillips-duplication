from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/movies')
def movies():
    return render_template('movies.html')




