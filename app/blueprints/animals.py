from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db



animals = Blueprint('animals', __name__)

@animals.route('/animal', methods=['GET', 'POST'])
def animal():
    db = get_db()
    cursor = db.cursor()


    # Handle POST request to add a new animal
    if request.method == 'POST':
        animal_name = request.form['animal_name']
        animal_type = request.form['animal_type']

        # Insert the new animal into the database
        cursor.execute('INSERT INTO animals (animal_name, animal_type) VALUES (%s, %s)', (animal_name, animal_type))
        db.commit()

        flash('New animal added successfully!', 'success')
        return redirect(url_for('animals.animal'))

    # Handle GET request to display all animals
    cursor.execute('SELECT * FROM animals')
    all_animals = cursor.fetchall()
    return render_template('animals.html', all_animals=all_animals)

@animals.route('/update_animal/<int:animal_id>', methods=['GET', 'POST'])
def update_animal(animal_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the animal's details
        animal_name = request.form['animal_name']
        animal_type = request.form['animal_type']

        cursor.execute('UPDATE animals SET animal_name = %s, animal_type = %s WHERE animal_id = %s',
                       (animal_name, animal_type, animal_id))
        db.commit()

        flash('Animal updated successfully!', 'success')
        return redirect(url_for('animals.animal'))

    # GET method: fetch animal's current data for pre-populating the form
    cursor.execute('SELECT * FROM animals WHERE animal_id = %s', (animal_id,))
    animal = cursor.fetchone()
    return render_template('update_animal.html', animal=animal)

@animals.route('/delete_animal/<int:animal_id>', methods=['POST'])
def delete_animal(animal_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the animal
    cursor.execute('DELETE FROM animals WHERE animal_id = %s', (animal_id,))
    db.commit()

    flash('Animal deleted successfully!', 'danger')
    return redirect(url_for('animals.animal'))
