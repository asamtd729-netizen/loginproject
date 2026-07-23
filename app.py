from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username, password) VALUES(?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    return render_template("dashboard.html")
app.run(debug=True)