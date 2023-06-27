from flask import Flask, render_template, session, request, redirect 
from flask_app import app
from flask_app.models import models_order

# GET Routes
# Cookie Orders HTML Route
@app.route('/')
@app.route('/cookies')
def index():
    return render_template('cookie_orders.html')

# New Order HTML Route
@app.route('/cookies/new')
def new_order():
    models_order.Order.save(request.form)
    return render_template('create_order.html')

# Edit Order HTML Route
@app.route('/cookies/edit/<order_id>')
def edit_order(order_id):
    data = {
        "id": id
    }
    return render_template('edit_order.html', order = models_order.Order.get_one(data))

# POST (ACTION) Routes
# Processes the create order route
@app.route('/cookies/create', methods=['POST'])
def create_order():
    models_order.Order.save(request.form)
    return redirect('/cookies')

# Processes the edit route
@app.route('/cookies/update', methods=['POST'])
def update_order():
    return redirect('/cookies')