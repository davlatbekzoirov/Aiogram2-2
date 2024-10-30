import sqlite3

class DatabaseRu:
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
        CREATE TABLE IF NOT EXISTS usersRu (
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
        INSERT INTO usersRu(id, name, password) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, password), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM usersRu
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM usersRu WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM usersRu;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM usersRu WHERE TRUE", commit=True)
