from db import db
from flask import session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if not user:
        # invalid username
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            # correct username and password
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            session["user_id"] = user.id
            return True
        else:
            # invalid password
            return False

def logout():
    del session["username"]
    del session["csrf_token"]
    del session["user_id"]

def create_account(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return True