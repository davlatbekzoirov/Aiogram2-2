import sqlite3
from datetime import datetime
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
        # connection.set_trace_callback(logger)
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

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id int NOT NULL,
            fullname varchar(255) NOT NULL,
            username varchar(255),
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

    def add_user(self, id: int, fullname: str, username: str):
        sql = """
        INSERT INTO Users(id, fullname, username) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, fullname, username), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


class UserBalanceDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                            (user_id INTEGER PRIMARY KEY, balance REAL)''')
        self.conn.commit()

    def update_balance(self, user_id, amount):
        current_balance = self.get_balance(user_id)
        new_balance = current_balance + float(amount)
        self.cursor.execute('UPDATE accounts SET balance = ? WHERE user_id = ?', (new_balance, user_id))
        self.conn.commit()

    def minus_balance(self, user_id, amount):
        current_balance = self.get_balance(user_id)
        new_balance = current_balance - float(amount)
        self.cursor.execute('UPDATE accounts SET balance = ? WHERE user_id = ?', (new_balance, user_id))
        self.conn.commit()

    def set_balance(self, user_id, amount):
        self.cursor.execute('INSERT OR REPLACE INTO accounts (user_id, balance) VALUES (?, ?)', (user_id, float(amount)))
        self.conn.commit()

    def get_balance(self, user_id):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            self.set_balance(user_id, 0)
            return 0
            

class ProductPriceDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_prices (
                product_name TEXT PRIMARY KEY,
                price REAL
            )
        """)
        self.conn.commit()

    def save_price(self, name, price):
        self.cursor.execute("REPLACE INTO product_prices (product_name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def get_price(self, name):
        self.cursor.execute("SELECT price FROM product_prices WHERE product_name=?", (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def close_connection(self):
        self.conn.close()

class SoldNumbers:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS numbers 
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              user_id TEXT,
                              data TEXT,
                              number TEXT)''')
        
    def save_number(self, user_id, data, number):
        existing_numbers = self.get_number(number)
        if existing_numbers:
            existing_data = existing_numbers[0][2]
            self.cursor.execute("UPDATE numbers SET data=? WHERE number=?", (data, number))
        else:
            self.cursor.execute("INSERT INTO numbers (user_id, data, number) VALUES (?,?,?)",
                                (user_id, data, number))
        self.connection.commit()

    def get_numbers(self, user_id):
        self.cursor.execute("SELECT number FROM numbers WHERE user_id=?", (user_id,))
        numbers = self.cursor.fetchall()
        numbers = [number[0] for number in numbers]
        return numbers

    def get_number(self, number):
        self.cursor.execute("SELECT * FROM numbers WHERE number=?", (number,))
        return self.cursor.fetchall()

    def count_users(self, user_id):
        self.cursor.execute("SELECT COUNT(*) FROM numbers WHERE user_id=?", (user_id,))
        count = self.cursor.fetchone()[0]
        return count

class PaymentChecker:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                                bill_id TEXT PRIMARY KEY,
                                amount INTEGER,
                                user_id TEXT
                            )''')
        self.conn.commit()

    def save_payment(self, bill_id, amount, user_id):
        self.cursor.execute('''INSERT INTO payments (bill_id, amount, user_id)
                               VALUES (?, ?, ?)''', (bill_id, amount, user_id))
        self.conn.commit()

    def get_payment(self, bill_id):
        self.cursor.execute('''SELECT user_id, bill_id, amount FROM payments
                               WHERE bill_id = ?''', (bill_id,))
        result = self.cursor.fetchone()
        if result:
            return list(result)
        else:
            return None

    def close(self):
        self.conn.close()


class Channel:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS channels
                                (username TEXT PRIMARY KEY,
                                 saved_time TEXT)''')
        self.conn.commit()

    def save_channel(self, username):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO channels VALUES (?, ?)", (username, current_time))
        self.conn.commit()

    def get_channels(self):
        self.cursor.execute("SELECT username FROM channels")
        return [row[0] for row in self.cursor.fetchall()]

    def get_time_channel(self, username):
        self.cursor.execute("SELECT saved_time FROM channels WHERE username=?", (username,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def del_channel(self, username):
        self.cursor.execute("SELECT username FROM channels WHERE username=?", (username,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("DELETE FROM channels WHERE username=?", (username,))
            self.conn.commit()
            return True
        else:
            return False
        

    def del_channels(self):
        self.cursor.execute("DELETE FROM channels")
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

class BanUser:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id TEXT)")
        self.conn.commit()
    def get_ban_users(self):
        self.cursor.execute("SELECT user_id FROM users")
        return [row[0] for row in self.cursor.fetchall()]
    def ban_user(self, user_id):
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        self.conn.commit()

    def check_user(self, user_id):
        self.cursor.execute("SELECT COUNT(*) FROM users WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def del_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
        self.conn.commit()

        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def del_users(self):
        self.cursor.execute("DELETE FROM users")
        self.conn.commit()

    def get_user(self, place):
        self.cursor.execute("SELECT user_id FROM users ORDER BY ROWID ASC LIMIT 1 OFFSET ?", (place - 1,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def count_users(self):
        self.cursor.execute("SELECT COUNT(*) FROM users")
        result = self.cursor.fetchone()
        return result[0]

    def __del__(self):
        self.cursor.close()
        self.conn.close()


class StateBot:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS states (id INTEGER PRIMARY KEY, state INTEGER)")

    def change(self, state):
        self.cursor.execute("INSERT INTO states (state) VALUES (?)", (int(state),))
        self.conn.commit()

    def get(self):
        self.cursor.execute("SELECT state FROM states ORDER BY id DESC LIMIT 1")
        result = self.cursor.fetchone()
        if result:
            return bool(result[0])
        return None

    def __del__(self):
        self.conn.close()