import sqlite3
from aiogram.dispatcher import FSMContext

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    async def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            name varchar(255) NOT NULL,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    async def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, id: int, name: str):
        sql = """
        INSERT INTO Users(id, name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(id, name), commit=True)

    async def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    async def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    async def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


class AnswersDatabase:
    def __init__(self, path_to_db="answers.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    async def create_table_user_answers(self):
        sql = """
        CREATE TABLE UserAnswers (
            user_id INTEGER,
            question_id INTEGER,
            user_answer TEXT,
            PRIMARY KEY (user_id, question_id)
            );
        """
        self.execute(sql, commit=True)

    async def add_user_answer(self, user_id: int, question_id: int, user_answer: str):
        sql = """
        INSERT INTO UserAnswers(user_id, question_id, user_answer) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, question_id, user_answer), commit=True)

    async def get_user_answers(self, user_id: int):
        sql = """
        SELECT question_id, user_answer FROM UserAnswers WHERE user_id = ?
        """
        return self.execute(sql, parameters=(user_id,), fetchall=True)

    
    async def calculate_score(self, state: FSMContext):
        data = await state.get_data()
        user_answers = data.get('answers', [])  
        score = 0
        for question_id, user_answer in enumerate(user_answers, start=1):
            correct_answer = self.get_user_answers(question_id)
            if user_answer == correct_answer:
                score += 1
        return score

