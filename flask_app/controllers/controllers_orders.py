from flask import Flask, render_template, session, request
from flask_app import app
from flask_app.models.models_order import Order

# cookies_orders HTML Route
@app.route('/')
@app.route('/cookies')
def index():
    return render_template('cookie_orders.html')

# create_order HTML Route
@app.route('/cookies/new')
def new_order():
    return render_template('create_order.html', methods=['POST'])

# edit_order HTML Route
@app.route('/cookies/edit/<order_id>')
def edit_order(order_id):
    return render_template('edit_order.html')