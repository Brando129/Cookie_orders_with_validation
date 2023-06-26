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

    # classmethod for saving a new cookie order
    @classmethod
    def save(cls, data):
        query = """ INSERT INTO orders (name, cookie_type, num_of_boxes)
                VALUES %(name)s, %(cookie_type)s, %(num_of_boxes)s;"""
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

    # classmethod for deleting an order
    @classmethod
    def destroy(cls, data):
        query = " DELETE FROM orders WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)