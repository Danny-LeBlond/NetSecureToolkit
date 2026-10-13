# Filename: modules/sql_demo_secure.py

"""
Secure SQL Demo Module

This program is a small Flask web app that shows a safer way to handle login
with SQL. It uses the same database and login page as the vulnerable version
but it fixes the problem by using a safer query method.

Functions:
    init_db()
    home()
    login()
    dump()

What it does:
    - Creates a SQLite database called users.db
    - Makes a users table if it does not already exist
    - Adds test users to the database
    - Shows a login page in the browser
    - Uses a parameterized query instead of putting user input directly into SQL
    - Prevents SQL injection in the login system

"""


from flask import Flask, request
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("DELETE FROM users")

    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user', '1234')")

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return """
    <h2>Login Page (SECURE)</h2>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit" value="Login">
    </form>
    """


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # this fixes sql injection by not letting user input change the query
    query = "SELECT * FROM users WHERE username=? AND password=?"

    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        return "Login successful"
    else:
        return "Login failed"


@app.route("/dump")
def dump():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    conn.close()

    return str(rows)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)