from flask_app.config.mysqlconnection import connectToMySQL
from  flask import Flask , abort

class User:
    db_name = 'User001Users'
    def __init__( self , data ):
        self.id = data['id']
        self.position = data['position']
        self.username = data['username']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return results

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s and  users.password = %(password)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return results
#=================================================================================================================#
#======================================= Admin                   =================================================#
#=================================================================================================================#
    @classmethod
    def if_its_admin(cls, data):
        query = "SELECT position , username FROM users WHERE position = 1  "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return results
    
    @classmethod
    def check_admin_status(cls,data):
        query = "SELECT * FROM users WHERE users.position = 1 and id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return results

#=================================================================================================================#
#======================================= For Pages posts by users =================================================#
#=================================================================================================================#

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if len(result) < 1:
            return False
        return result[0]
    
    @classmethod
    def get_all_user_info(cls, data):
        query= 'SELECT * FROM users LEFT JOIN posts on posts.user_id = users.id WHERE users.id = %(user_id)s;'
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        posts = []
        for row in results:
            posts.append(row)
        return posts
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        if results:
            for user in results:
                users.append(user)
            return users
        return users
    #CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (position, username, password,email) VALUES ( %(position)s, %(username)s, %(password)s,%(email)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)  
    
    #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE users.id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)  
    
    #DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE users.id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)