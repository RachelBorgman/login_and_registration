from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email must be at least 3 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if not any(char.isdigit() for char in user['password']):
            flash('Password should have at least one number')
            is_valid = False
        if not any(char.isupper() for char in user['password']):
            flash('Password should have at least one uppercase letter')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(user):
        is_valid = True
        if len(user['username']) < 3:
            flash("Login Username must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("Login Email must be at least 3 characters.")
            is_valid = False
        if len(user['password']) < 3:
            flash("Login Password must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Login Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, username, password) VALUES (%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s);"
        return connectToMySQL('users').query_db(query, data)


#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM users;"
#         results = connectToMySQL('users_schema').query_db(query)
#         users = []
#         for u in results:
#             users.append(cls(u))
#         return users
    
#     @classmethod
#     def get_one(cls, data):
#         query = """
#                 SELECT * FROM users
#                 WHERE id = %(id)s;
#         """
#         result = connectToMySQL('users_schema').query_db(query, data)
#         return cls(result[0])
    
#     @classmethod
#     def update(cls,data):
#         query = """
#             UPDATE users
#             SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW()
#             WHERE id = %(id)s;
#         """
#         results = connectToMySQL('users_schema').query_db(query, data)
#         return results
    
#     @classmethod
#     def delete(cls, data):
#         query = "DELETE FROM users WHERE id = %(id)s;"
#         results = connectToMySQL('users_schema').query_db(query, data)
#         return results

#     @classmethod
#     def save(cls, data):
#         query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
#         # data is a dictionary that will be passed into the save method from server.py
#         return connectToMySQL('users_schema').query_db(query, data)