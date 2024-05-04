from app import app
from flask import redirect, render_template, request, session, abort, flash
import users
import courses

@app.route("/")
def index():
    course_list = courses.get_courses()
    allow = users.check_rights()
    return render_template("index.html", course_list=course_list, allow=allow) 

@app.route("/form") #log in
def form():
    return render_template("form.html")

@app.route("/create") #register
def create():
    return render_template("create.html")

@app.route("/login", methods=["POST"])
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

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1==password2:
        if len(password1)>7:
            if users.create_account(username, password1):
                flash("Käyttäjätunnuksen luominen onnistui")
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
        if content!="":
            if courses.send_feedback(id, content):
                course = courses.get_course(id)
                feedback_list = courses.get_feedback(id)
                flash("Arvostelun tallennus onnistui")
                return render_template("feedback.html", id=id, course=course, feedback_list=feedback_list)
            else:
                return render_template("error.html", message="Arvostelun jättäminen epäonnistui")
        else:
            return render_template("error.html", message="Arvostelun jättäminen epäonnistui, kirjoita lähetettävä arvostelu")

@app.route("/diary", methods=["GET", "POST"])
def diary():
    if request.method == "GET":
        if "csrf_token" not in session:
            abort(403)
        user_id = session["user_id"]
        diary_list = courses.get_diary()
        return render_template("diary.html", user_id=user_id, diary_list=diary_list)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        id = session["user_id"]
        content = request.form["content"]
        if content!="":
            if courses.send_diary(id, content):
                diary_list = courses.get_diary()
                flash("Merkinnän tallennus onnistui")
                return render_template("diary.html", id=id, diary_list=diary_list)
            else:
                return render_template("error.html", message="Merkinnän kirjaaminen epäonnistui")
        else:
            return render_template("error.html", message="Merkinnän kirjaaminen epäonnistui, kirjoita tallennettava merkintä")

@app.route("/add_course", methods=["GET", "POST"])
def add_course():
    if request.method == "GET":
        if "csrf_token" not in session or session["user_rights"]!="admin":
            abort(403)
        return render_template("add_course.html")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        sport = request.form["sport"]
        course_name = request.form["course_name"]
        instructor = request.form["instructor"]
        max_enrollments = request.form["max_enrollments"]
        # if max_enrollments<10 or max_enrollments>100:
        #     flash("Kurssin osallistujamäärä on virheellinen")
        #     return render_template("add_course.html")
        event_time = request.form["event_time"]
        place = request.form["place"]
        difficulty = request.form["difficulty"]
        if courses.add_course(sport, course_name, instructor, max_enrollments, event_time, place, difficulty):
            flash("Kurssin lisääminen onnistui")
            return redirect("/")
        else:
            return render_template("error.html", message="Kurssin lisääminen epäonnistui")
        
@app.route("/remove_course/<int:id>")
def remove_course(id):
    if "csrf_token" not in session or session["user_rights"]!="admin":
        abort(403)
    if courses.remove_course(id):
        flash("Kurssin poistaminen onnistui")
        return redirect("/")
    else:
        return render_template("error.html", message="Kurssin poistaminen epäonnistui")