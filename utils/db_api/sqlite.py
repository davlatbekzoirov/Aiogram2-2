import sqlite3
from data import config
import datetime

class Database:
    def __init__(self, path_to_db="mainru.db"):
        self.path_to_db = path_to_db
        self.connection = None

    def open_connection(self):
        self.connection = sqlite3.connect(self.path_to_db)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not self.connection:
            self.open_connection()

        if not parameters:
            parameters = ()
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, parameters)
            if commit:
                self.connection.commit()
            if fetchall:
                return cursor.fetchall()
            if fetchone:
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            if not fetchone and not fetchall:
                self.close_connection()

    def create_table_users(self):
        sql = """
        CREATE TABLE users (
            id INTEGER NOT NULL,
            name TEXT NOT NULL,
            password TEXT,
            PRIMARY KEY (id)
            );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, password: str):
        sql = """
        INSERT INTO users(id, name, password) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, password), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM users WHERE TRUE", commit=True)

class Add_post:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.connect()
        self.cursor.execute(
            """
            CREATE TABLE posts (
                id INTEGER PRIMARY KEY,
                text TEXT,
                image_path TEXT,
                name_course TEXT
            );
            """
        )
        self.conn.commit()
        self.close()

    def add_post(self, text, image_path, name_course):
        self.connect()
        sql = "INSERT INTO posts (text, image_path, name_course) VALUES (?, ?, ?)"
        self.cursor.execute(sql, parameters=(text, image_path, name_course), commit=True)
        self.conn.commit()
        self.close()


    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


class Add_post_Uz:
    def __init__(self, path_to_db="UzPost.db"):
        self.path_to_db = path_to_db
        self.connection = None

    def open_connection(self):
        self.connection = sqlite3.connect(self.path_to_db)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not self.connection:
            self.open_connection()

        if not parameters:
            parameters = ()
            cursor = self.connection.cursor()
        try:
            cursor.execute(sql, parameters)
            if commit:
                self.connection.commit()
            if fetchall:
                return cursor.fetchall()
            if fetchone:
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            if not fetchone and not fetchall:
                self.close_connection()

    def create_tableUz(self):
        sql ="""
            CREATE TABLE postsUz (
                id SERIAL PRIMARY KEY,

                category_code VARCHAR(20) NOT NULL,
                category_name VARCHAR(50) NOT NULL,

                subcategory_code VARCHAR(20) NOT NULL,
                subcategory_name VARCHAR(50) NOT NULL,

                photo varchar(255) NULL,
                description VARCHAR(3000) NULL
                );
            """
        self.execute(sql, commit=True)

    def add_postUz(
        self,
        category_name,
        photo=None,
        description="",
    ):
        sql = "INSERT INTO postsUz (category_name,photo, description) VALUES(?, ?, ?)"
        self.execute(sql, parameters=(category_name,photo, description), commit=True)

    def select_all_posts(self):
        sql = """
        SELECT * FROM postsUz
        """
        return self.execute(sql, fetchall=True)
    
    def get_categories(self):
        sql = "SELECT DISTINCT category_name, category_code FROM postsUz"
        return self.execute(sql, fetchall=True)
    
    def get_subcategories(self, category_code):
        sql = f"SELECT DISTINCT subcategory_name, subcategory_code FROM postsUz WHERE category_code='{category_code}'"
        return self.execute(sql, fetchall=True)
    
    def count_products(self, category_code, subcategory_code=None):
        if subcategory_code:
            sql = f"SELECT COUNT(*) FROM postsUz WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        else:
            sql = f"SELECT COUNT(*) FROM postsUz WHERE category_code='{category_code}'"
        return self.execute(sql, fetchone=True)
    
    def get_products(self, category_code, subcategory_code):
        sql = f"SELECT * FROM postsUz WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        return self.execute(sql, fetchall=True)

    def get_product(self, product_id):
        sql = f"SELECT * FROM postsUz WHERE id={product_id}"
        return self.execute(sql, fetchone=True)

    def drop_products(self):
        self.execute("DROP TABLE postsUz", commit=True)