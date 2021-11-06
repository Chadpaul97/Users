from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save_user(cls,data):
        query="INSERT into users (first_name,last_name,email) VALUES(%(first_name)s,%(last_name)s,%(email)s)"
        return connectToMySQL("user_schema").query_db(query,data)

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM users"
        query_results = connectToMySQL("user_schema").query_db(query)
        users=[]
        for user in query_results:
            new_user = cls(user)
            users.append(new_user)
        return users

