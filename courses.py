from db import db
from flask import session
from sqlalchemy.sql import text
import users

def get_courses():
    if session.get("username"):
        user_id = users.get_user_id()
        sql = text("SELECT C.id, C.course_name, C.event_time, C.place, C.difficulty, E.course_id FROM courses C LEFT JOIN enrollments E ON C.id=E.course_id AND E.user_id=:user_id")
        result = db.session.execute(sql, {"user_id":user_id})
        return result.fetchall()
    else:
        sql = text("SELECT id, course_name, event_time, place, difficulty FROM courses")
        result = db.session.execute(sql)
        return result.fetchall()

def get_course(id):
    sql = text("SELECT id, course_name, event_time, place FROM courses WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def enroll(id):
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":session["username"]})
    user_id = result.fetchone()[0]
    sql = text("SELECT COUNT(course_id) FROM enrollments WHERE user_id=:user_id AND course_id=:course_id")
    result = db.session.execute(sql, {"course_id":id, "user_id":user_id})
    counter = result.fetchone()[0]
    if counter<1:
        try:
            sql = text("INSERT INTO enrollments (course_id, user_id) VALUES (:course_id, :user_id)")
            db.session.execute(sql, {"course_id":id, "user_id":user_id})
            db.session.commit()
        except:
            return False
        return True
    else:
        return False

def undo_enroll(id):
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":session["username"]})
    user_id = result.fetchone()[0]
    try:
        sql = text("DELETE FROM enrollments WHERE user_id=:user_id AND course_id=:course_id")
        db.session.execute(sql, {"course_id":id, "user_id":user_id})
        db.session.commit()
    except:
        return False
    return True

def get_feedback(id):
    sql = text("SELECT id, content FROM feedback WHERE course_id=:course_id")
    result = db.session.execute(sql, {"course_id":id})
    return result.fetchall()

def send_feedback(id, content):
    try:
        sql = text("INSERT INTO feedback (course_id, content) VALUES (:course_id, :content)")
        db.session.execute(sql, {"course_id":id, "content":content})
        db.session.commit()
    except:
        return False
    return True

def get_diary():
    user_id = users.get_user_id()
    sql = text("SELECT id, created_at, content FROM diary WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def send_diary(id, content):
    try:
        sql = text("INSERT INTO diary (user_id, created_at, content) VALUES (:user_id, NOW(), :content)")
        db.session.execute(sql, {"user_id":id, "content":content})
        db.session.commit()
    except Exception as error:
        print(error)
        return False
    return True