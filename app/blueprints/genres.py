# app/blueprints/genres.py
from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

genres = Blueprint('genres', __name__)

@genres.route('/genres', methods=['GET', 'POST'])
def genre():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new genre
    if request.method == 'POST':
        genre_name = request.form['genre_name']

        # Insert the new genre into the database
        cursor.execute('INSERT INTO genres (genre_name) VALUES (%s)', (genre_name,))
        db.commit()

        flash('New genre added successfully!', 'success')
        return redirect(url_for('genres.genre'))

    # Handle GET request to display all genres
    cursor.execute('SELECT * FROM genres')
    all_genres = cursor.fetchall()
    return render_template('genres.html', all_genres=all_genres)

@genres.route('/update_genre/<int:genre_id>', methods=['GET', 'POST'])
def update_genre(genre_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the genre's details
        genre_name = request.form['genre_name']

        cursor.execute('UPDATE genres SET genre_name = %s WHERE id = %s', (genre_name, genre_id))
        db.commit()

        flash('Genre updated successfully!', 'success')
        return redirect(url_for('genres.genre'))

    # GET method: fetch genre's current data for pre-populating the form
    cursor.execute('SELECT * FROM genres WHERE id = %s', (genre_id,))
    genre = cursor.fetchone()
    return render_template('update_genre.html', genre=genre)

@genres.route('/delete_genre/<int:genre_id>', methods=['POST'])
def delete_genre(genre_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the genre
    cursor.execute('DELETE FROM genres WHERE id = %s', (genre_id,))
    db.commit()

    flash('Genre deleted successfully!', 'danger')
    return redirect(url_for('genres.genre'))

