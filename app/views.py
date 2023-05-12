from flask import render_template, request, redirect, url_for
from app import app
from app.models import FoodItem


@app.route('/')
def home():
    food_items = FoodItem.get_all()
    return render_template('home.html', food_items=food_items)


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form.get('name')
        expiry_date = request.form.get('expiry_date')

        food_item = {
            'name': name,
            'expiry_date': expiry_date
        }

        FoodItem.create(food_item)
        return redirect(url_for('home'))

    return render_template('add_item.html')


@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    food_item = FoodItem.get_by_id(item_id)

    if request.method == 'POST':
        name = request.form.get('name')
        expiry_date = request.form.get('expiry_date')

        updates = {
            'name': name,
            'expiry_date': expiry_date
        }

        FoodItem.update(item_id, updates)
        return redirect(url_for('home'))

    return render_template('edit_item.html', item=food_item)


@app.route('/delete/<item_id>', methods=['POST'])
def delete_item(item_id):
    FoodItem.delete(item_id)
    return redirect(url_for('home'))
