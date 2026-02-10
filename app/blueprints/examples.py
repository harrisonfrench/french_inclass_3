from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

examples = Blueprint('examples', __name__)

@examples.route('/', methods=['GET', 'POST'])
def show_examples():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new bear
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        habitat = request.form['habitat']

        # Insert the new bear into the database
        cursor.execute('INSERT INTO bears (name, species, age, habitat) VALUES (%s, %s, %s, %s)',
                       (name, species, age, habitat))
        db.commit()

        flash('New bear added successfully!', 'success')
        return redirect(url_for('examples.show_examples'))

    # Handle GET request to display all bears
    cursor.execute('SELECT * FROM bears')
    all_bears = cursor.fetchall()
    return render_template('examples.html', all_bears=all_bears)

@examples.route('/update_bear/<int:bear_id>', methods=['POST'])
def update_bear(bear_id):
    db = get_db()
    cursor = db.cursor()

    # Update the bear's details
    name = request.form['name']
    species = request.form['species']
    age = request.form['age']
    habitat = request.form['habitat']

    cursor.execute('UPDATE bears SET name = %s, species = %s, age = %s, habitat = %s WHERE bear_id = %s',
                   (name, species, age, habitat, bear_id))
    db.commit()

    flash('Bear updated successfully!', 'success')
    return redirect(url_for('examples.show_examples'))

@examples.route('/delete_bear/<int:bear_id>', methods=['POST'])
def delete_bear(bear_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the bear
    cursor.execute('DELETE FROM bears WHERE bear_id = %s', (bear_id,))
    db.commit()

    flash('Bear deleted successfully!', 'danger')
    return redirect(url_for('examples.show_examples'))

