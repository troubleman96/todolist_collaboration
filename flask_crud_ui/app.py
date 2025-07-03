from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def index():
    if 'token' not in session:
        return redirect(url_for('login'))
    # Render dashboard template without tasks data (tasks loaded from FastAPI)
    return render_template("dashboard.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/save_token", methods=["POST"])
def save_token():
    token = request.json.get("token")
    session["token"] = token
    return jsonify({"message": "Token saved"})

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
