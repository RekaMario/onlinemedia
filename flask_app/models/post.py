from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Post:
    db_name = 'User001Users'
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.subtitle = data['subtitle']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image = data['image']
        self.categories = data['categories']


    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of users
        posts = []
        if results:
        # Iterate over the db results and create instances of friends with cls.
            for post in results:
                posts.append(post)
            return posts
        return posts
    
    @classmethod
    def get_post_by_id(cls, data):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id WHERE posts.id = %(post_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return results
    
    #CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (title, subtitle, content,user_id,categories) VALUES ( %(title)s, %(subtitle)s , %(content)s,%(user_id)s,%(categories)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)  

    #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET title = %(title)s, subtitle = %(subtitle)s, content = %(content)s,categories = %(categories)s  WHERE posts.id = %(post_id)s and user_id= %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)  

    #DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE posts.id = %(post_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_all_user_posts(cls, data):
        query = "DELETE FROM posts WHERE posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def add_post_image(cls, data):
        query = "UPDATE posts SET image = %(image)s WHERE id = %(id)s and posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def add_post_video(cls, data):
        query = "UPDATE posts SET video = %(video)s WHERE id = %(id)s and posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
        
    @classmethod
    def add_post_instaembed(cls, data):
        query = "UPDATE posts SET instaembed = %(instaembed)s WHERE id = %(id)s and posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def add_post_yturl(cls, data):
        query = "UPDATE posts SET yturl = %(yturl)s WHERE id = %(id)s and posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def add_post_fburl(cls, data):
        query = "UPDATE posts SET fburl = %(fburl)s WHERE id = %(id)s and posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def add_post_tturl(cls, data):
        query = "UPDATE posts SET tturl = %(tturl)s WHERE id = %(id)s and posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_post_by_id(cls, data):
        query= 'SELECT * FROM posts WHERE posts.id = %(post_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]

    @classmethod
    def get_user_posts(cls):
        query= 'SELECT * FROM users LEFT JOIN posts on posts.user_id = %(user_id)s WHERE users.id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query)
        posts = []
        if results:
            for post in results:
                posts.append(post)
            return posts
        return posts
    
    
    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['content']) < 2:
            flash("Post content must be at least 2 characters.", 'content')
            is_valid = False
        return is_valid

#=================================================================================================================#
#======================================= For Pages used by users =================================================#
#=================================================================================================================#
    @classmethod
    def get_post(cls, data):
        query= 'select * from posts order by  posts.created_at desc LIMIT 30'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        posts = []
        for row in results:
            posts.append(row)
        return posts

    @classmethod
    def get_post_by_categories(cls, data):
        query= 'select id, title , content ,subtitle,created_at ,image , categories ,video from posts where  posts.categories=%(categories)s order by  posts.created_at desc'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        posts = []
        for row in results:
            posts.append(row)
        return posts
    
    @classmethod
    def get_last_2_posts(cls, categories):
        query = "SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC LIMIT 2"
        data = {'categories': categories}
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_last_3_posts(cls, categories):
        query = "SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC LIMIT 3"
        data = {'categories': categories}
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
        
    @classmethod
    def get_last_4_posts(cls, categories):
        query = "SELECT id, title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC LIMIT 4"
        data = {'categories': categories}
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_last_5_posts(cls, data):
        query = " SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC  LIMIT 5 "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_last_10_posts(cls, data):
        query = " SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC  LIMIT 10 "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
    
    @classmethod
    def get_last_1_posts(cls, data):
        query = " SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC  LIMIT 1 "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
    
    @classmethod
    def get_last_posts(cls, categories):
        query = "SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC LIMIT 1"
        data = {'categories': categories}
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
    
    @classmethod
    def get_second_posts(cls, data):
        query = " SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC  LIMIT 1  OFFSET 1 "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
    
    @classmethod
    def get_third_posts(cls, data):
        query = " SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC  LIMIT 1  OFFSET 2 "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
        
    @classmethod
    def get_forth_posts(cls, data):
        query = " SELECT id,title, content, subtitle, created_at, updated_at, image, categories, video FROM posts WHERE categories = %(categories)s ORDER BY updated_at DESC  LIMIT 1  OFFSET 3 "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
#=================================================================================================================#
#======================================= For Pages used by users =================================================#
#=================================================================================================================#
    
    @classmethod
    def count_posts(cls):
        query = "SELECT COUNT(*) as count FROM posts"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result[0]['count']
    
    @classmethod
    def count_posts_by_category(cls):
        query = "SELECT id,categories, COUNT(*) as count FROM posts GROUP BY categories"
        results = connectToMySQL(cls.db_name).query_db(query)
        counts_by_category = {}
        for result in results:
            category = result['categories']
            count = result['count']
            counts_by_category[category] = count
        return counts_by_category
