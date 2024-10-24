from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/genres')
def genres():
    return render_template('genres.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/filters')
def filters():
    return render_template('filters.html')





