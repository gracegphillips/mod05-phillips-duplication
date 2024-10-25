# app/blueprints/movie_genres.py
from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db
from ..functions import filter_movies_by_genre

movie_genres = Blueprint('movie_genres', __name__)

@movie_genres.route('/filter_by_genre', methods=['POST'])
def filter_by_genre():
    genre_id = request.form.get('genre_id')
    filtered_movies = filter_movies_by_genre(genre_id)
    return render_template('filters.html', all_movies=filtered_movies)


@movie_genres.route('/movie_genres', methods=['GET', 'POST'])
def movie_genre():
    db = get_db()
    cursor = db.cursor()

  # Handle POST request to add a new movie-genre association
    if request.method == 'POST':
        movie_id = request.form['movie_id']
        genre_id = request.form['genre_id']

        # Insert the new movie-genre association into the database
        cursor.execute('INSERT INTO movie_genres (movie_id, genre_id) VALUES (%s, %s)', (movie_id, genre_id))
        db.commit()

        flash('New movie-genre association added successfully!', 'success')
        return redirect(url_for('movie_genres.movie_genre'))

    # Handle GET request to display all movie-genre associations
    cursor.execute('SELECT * FROM movie_genres')
    all_movie_genres = cursor.fetchall()
    return render_template('movie_genres.html', all_movie_genres=all_movie_genres)