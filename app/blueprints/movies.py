from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db
from app.functions import filter_movies

movies = Blueprint('movies', __name__)


@movies.route('/filter_by_title', methods=['POST'])
def filter_by_title():
    title = request.form.get('title')
    filtered_movies = filter_movies(title=title)
    return render_template('filters.html', all_movies=filtered_movies)



@movies.route('/movies', methods=['GET', 'POST'])
def movie():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new movie
    if request.method == 'POST':
        title = request.form['title']
        release_year = request.form['release_year']


        # Insert the new movie into the database
        cursor.execute('INSERT INTO movies (title, release_year) VALUES (%s, %s)',
                       (title, release_year))
        db.commit()

        flash('New movie added successfully!', 'success')
        return redirect(url_for('movies.movie'))

    # Handle GET request to display all movies
    cursor.execute('SELECT * FROM movies')
    all_movies = cursor.fetchall()
    return render_template('movies.html', all_movies=all_movies)

@movies.route('/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the movie's details
        title = request.form['title']
        release_year = request.form['release_year']

        cursor.execute('UPDATE movies SET title = %s, release_year = %s WHERE id = %s',
                       (title, release_year, movie_id))
        db.commit()

        flash('Movie updated successfully!', 'success')
        return redirect(url_for('movies.movie'))

    # GET method: fetch movie's current data for pre-populating the form
    cursor.execute('SELECT * FROM movies WHERE id = %s', (movie_id,))
    movie = cursor.fetchone()
    return render_template('update_movie.html', movie=movie)

@movies.route('/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the movie
    cursor.execute('DELETE FROM movies WHERE id = %s', (movie_id,))
    db.commit()

    flash('Movie deleted successfully!', 'danger')
    return redirect(url_for('movies.movie'))


