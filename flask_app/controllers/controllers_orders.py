from flask import Flask, render_template, session, request
from flask_app import app
from flask_app.models.models_order import Order

# cookies_orders HTML Route
@app.route('/')
@app.route('/cookies')
def index():
    return render_template('cookie_orders.html')