import sqlite3

class DatabaseStart:
    def __init__(self, path_to_db="start.db"):
        self.path_to_db = path_to_db

    def executeStart(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        with sqlite3.connect(self.path_to_db) as connection:
            cursorStart = connection.cursor()
            cursorStart.execute(sql, parameters)

            if commit:
                connection.commit()

            if fetchall:
                data = cursorStart.fetchall()
            elif fetchone:
                data = cursorStart.fetchone()
            else:
                data = None

        return data

    def create_table_usersStart(self):
        sql = """
        CREATE TABLE IF NOT EXISTS usersStart (
            id INTEGER NOT NULL,
            fullname TEXT NOT NULL,
            username TEXT NOT NULL,
            PRIMARY KEY (id)
        );
        """
        self.executeStart(sql, commit=True)

    @staticmethod
    def format_argsStart(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_userStart(self, id: int, fullname: str, username: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, ) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO usersStart(id, fullname, username) VALUES(?, ?, ?)
        """
        self.executeStart(sql, parameters=(id, fullname, username), commit=True)

    def select_all_usersStart(self):
        sql = """
        SELECT * FROM usersStart
        """
        return self.executeStart(sql, fetchall=True)

    def select_userStart(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM usersStart WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.executeStart(sql, parameters=parameters, fetchone=True)

    def count_usersStart(self):
        return self.executeStart("SELECT COUNT(*) FROM usersStart;", fetchone=True)

    def delete_usersStart(self):
        self.executeStart("DELETE FROM usersStart WHERE TRUE", comStartt=True)
