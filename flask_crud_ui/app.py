from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# SQLite database file
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "tasks.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)

from models import Task

@app.route("/")
def index():
    if 'token' not in session:
        return redirect(url_for('login'))
    tasks = Task.query.all()
    return render_template("dashboard.html", tasks=tasks)

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/save_token", methods=["POST"])
def save_token():
    token = request.json.get("token")
    session["token"] = token
    return jsonify({"message": "Token saved"})


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/add", methods=["POST"])
def add_task():
    if 'token' not in session:
        return redirect(url_for('login'))
    title = request.form.get("title")
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 'token' not in session:
        return redirect(url_for('login'))
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
