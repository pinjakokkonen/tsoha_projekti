from db import db
from flask import session
from sqlalchemy.sql import text

def get_courses():
    sql = text("SELECT id, course_name, event_time, place FROM courses")
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