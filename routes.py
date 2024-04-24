from app import app
from flask import redirect, render_template, request, session, abort
import users
import courses

@app.route("/")
def index():
    course_list = courses.get_courses()
    return render_template("index.html", course_list=course_list) 

@app.route("/form") #log in
def form():
    return render_template("form.html")

@app.route("/create") #register
def create():
    return render_template("create.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # check username and password
    if users.login(username, password):
        return redirect("/")
    else:
        return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/create_account",methods=["POST"])
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1==password2:
        if len(password1)>7:
            if users.create_account(username, password1):
                return redirect("/")
            else:
                return render_template("error.html", message="Tunnuksen luominen epäonnistui")
        else:
            return render_template("error.html", message="Salasana on liian lyhyt")
    else:
        return render_template("error.html", message="Salasanat eroavat")
    
@app.route("/enroll/<int:id>", methods=["GET", "POST"])
def enroll(id):
    if request.method == "GET":
        if "csrf_token" not in session:
            abort(403)
        course = courses.get_course(id)
        return render_template("enroll.html", id=id, course=course)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if courses.enroll(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ilmoittautuminen epäonnistui")

@app.route("/unenroll/<int:id>")
def unenroll(id):
    if "csrf_token" not in session:
        abort(403)
    if courses.undo_enroll(id):
        return redirect("/")
    else:
        return render_template("error.html", message="Ilmoittautumisen peruminen epäonnistui")

@app.route("/feedback/<int:id>", methods=["GET", "POST"])
def feedbacks(id):
    if request.method == "GET":
        course = courses.get_course(id)
        feedback_list = courses.get_feedback(id)
        return render_template("feedback.html", id=id, course=course, feedback_list=feedback_list)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        content = request.form["content"]
        if courses.send_feedback(id, content):
            course = courses.get_course(id)
            feedback_list = courses.get_feedback(id)
            return render_template("feedback.html", id=id, course=course, feedback_list=feedback_list)
        else:
            return render_template("error.html", message="Arvostelun jättäminen epäonnistui")