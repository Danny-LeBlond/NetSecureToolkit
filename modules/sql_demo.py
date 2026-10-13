# Filename: modules/sql_demo.py

"""
Vulnerable SQL Demo Module

This program is a small Flask web app that shows how SQL injection can happen.
It creates a simple users database, shows a login page and uses an unsafe SQL
query that directly trusts what the user types.

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
    - Uses a string formatted SQL query that puts user input directly into the query
    - Lets the user test SQL injection and see how it can break the login

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

    # clear old data so it doesn't duplicate every run
    cursor.execute("DELETE FROM users")

    # test users
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user', '1234')")

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return """
    <h2>Login Page (Vulnerable)</h2>
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

    # VULNERABLE QUERY
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Running query:", query)

    cursor.execute(query)
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
    print("Database initialized")
    app.run(debug=True)