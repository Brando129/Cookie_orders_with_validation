from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models import models_order

# GET Routes
# Cookie Orders HTML Route
# @app.route('/')
# @app.route('/cookies')
# def index():
#     all_orders = models_order.Order.get_all('data')
#     return render_template('cookie_orders.html', orders = all_orders)

# New Order HTML Route
@app.route('/cookies/new')
def new_order():
    models_order.Order.save(request.form)
    return render_template('create_order.html')

# Edit Order HTML Route
@app.route('/cookies/edit/<int:id>')
def edit_order(id):
    data = {
        "id": id
    }
    return render_template('edit_order.html', order = models_order.Order.get_one(data))

# POST (ACTION) Routes
# Processes the create order route
@app.route('/cookies/create', methods=['POST'])
def create_order():
    if models_order.Order.validate_order(request.form):
        models_order.Order.save(request.form)
        return redirect('/cookies')
    return redirect('/cookies/new')

# Processes the edit route
@app.route('/cookies/update', methods=['POST'])
def update_order():
    if models_order.Order.validate_order(request.form):
        models_order.Order.update(request.form)
        return redirect('/cookies')
    return redirect("/cookies/edit/id")

@app.route('/cookies/destroy/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    models_order.Order.destroy(data)
    return redirect('/cookies')