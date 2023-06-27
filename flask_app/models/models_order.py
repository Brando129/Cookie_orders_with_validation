from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# Database name
db = "cookie_schema"

class Order:
    def __init__(self, data):
        # Always match these names with database table names
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.orders = []

    # classmethod for getting all the cookie orders
    @classmethod
    def get_all(cls, data):
        all_orders_list = []
        query = "SELECT * FROM orders;"
        all_orders_data = connectToMySQL(db).query_db(query)

        for order in all_orders_data:
            new_order = Order(order)
            all_orders_list.append(new_order)
        return all_orders_list

    # classmethod for saving a new cookie order
    @classmethod
    def save(cls, data):
        query = """ INSERT INTO orders (name, cookie_type, num_of_boxes)
                VALUES (%(name)s, %(cookie_type)s, %(num_of_boxes)s);"""
        return connectToMySQL(db).query_db(query, data)

    # classmethod for selecting a cookie order to edit
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    # classmethod for updating a cookie order
    @classmethod
    def update(cls, data):
        query = """UPDATE orders SET name=%(name)s, cookie_type=%(cookie_type)s,
                num_of_boxes=%(num_of_boxes)s, updated_at=NOW() WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query, data)

    # staticmethod for validating an Order
    @staticmethod
    def validate_order(data):
        is_valid = True
        if len(data['name']) == 0:
            flash("We need a name.")
            is_valid = False
        if len(data['cookie_type']) == 0:
            flash("We need a cookie type.")
            is_valid = False
        if len(data['num_of_boxes']) == 0:
            flash("We need the number of boxes.")
            is_valid = False
        elif int(data['num_of_boxes']) <= 0:
            flash("Number of boxes must be more than 0.")
            is_valid = False
        return is_valid