from flask import Flask, render_template, session, request, redirect
import database

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template ("/index.html")

@app.route("/about")
def about():
    return render_template ("/about.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return "LOGIN PAGE"
    elif request.method == "POST":
        username = request.form.get("username")
        if (database.authenticate(username, request.form.get("password"))):
            session['user'] = hashlib.sha224(username)
            session.save()
            return redirect("/")

@app.route("/signup")
def signup():
    return "SIGNUP PAGE"

@app.route("/logout")
def logout():
    session.delete()
    return "LOGOUT PAGE"

@app.route("/post")
def post():
    return "INDIVIDUAL POST"

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gottacatch'emall"
    app.run()
