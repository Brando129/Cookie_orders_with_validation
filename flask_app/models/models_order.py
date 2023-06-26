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