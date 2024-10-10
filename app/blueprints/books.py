# app/blueprints/books.py
from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

books = Blueprint('books', __name__)

@books.route('/books', methods=['GET', 'POST'])
def book():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new book
    if request.method == 'POST':
        book_title = request.form['book_title']
        book_genre = request.form['book_genre']
        book_author = request.form['book_author']

        # Insert the new book into the database
        cursor.execute('INSERT INTO books (book_title, book_genre, book_author) VALUES (%s, %s, %s)',
                       (book_title, book_genre, book_author))
        db.commit()

        flash('New book added successfully!', 'success')
        return redirect(url_for('books.book'))

    # Handle GET request to display all books
    cursor.execute('SELECT * FROM books')
    all_books = cursor.fetchall()
    return render_template('books.html', all_books=all_books)

@books.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the book's details
        book_title = request.form['book_title']
        book_genre = request.form['book_genre']
        book_author = request.form['book_author']

        cursor.execute('UPDATE books SET book_title = %s, book_genre = %s, book_author = %s WHERE book_id = %s',
                       (book_title, book_genre, book_author, book_id))
        db.commit()

        flash('Book updated successfully!', 'success')
        return redirect(url_for('books.book'))

    # GET method: fetch book's current data for pre-populating the form
    cursor.execute('SELECT * FROM books WHERE book_id = %s', (book_id,))
    book = cursor.fetchone()
    return render_template('update_book.html', book=book)

@books.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the book
    cursor.execute('DELETE FROM books WHERE book_id = %s', (book_id,))
    db.commit()

    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('books.book'))
