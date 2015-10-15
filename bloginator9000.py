from flask import Flask, render_template, session, request, redirect
import database, hashlib

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template ("/blog.html")

@app.route("/about")
def about():
    return render_template ("/about.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("/login.html")
    else:
        username = request.form.get("login")
        if (database.authenticate(username, request.form.get("password"))):
            session['user'] = username
            #session.save()
            return redirect("/")
        else:
            return "Incorrect username and/or password"

@app.route("/register", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        if request.form.get("password") == request.form.get("password2"):
            if database.newUser(request.form.get("login"), request.form.get("password")):
                return redirect("/")
            else:
                return "This username has already been taken"
        else:
            return "Your passwords do not match"

@app.route("/logout")
def logout():
    del session['user']
    return "LOGOUT PAGE"

@app.route("/post")
def post():
    return "INDIVIDUAL POST"

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gottacatch'emall"
    app.run()
