from app import app
from db import db
from flask import redirect, render_template, request, session
from os import getenv
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if not user:
        # TODO: invalid username
        pass
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            # TODO: correct username and password
            session["username"] = username
        else:
            # TODO: invalid password
            pass
    return redirect("/form")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/create_account",methods=["POST"])
def create_account():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()
    return redirect("/")