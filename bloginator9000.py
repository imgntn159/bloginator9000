from flask import Flask, render_template, session, request, redirect
import database, hashlib

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/blog")
def index():
    return render_template ("/blog.html", current_user = session.get('user'),  blogitems = database.getPosts())

@app.route("/about")
def about():
    return render_template ("/about.html", current_user = session.get('user'))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("/login.html")
    else:
        username = request.form.get("login")
        if (database.authenticate(username, request.form.get("password"))):
            session['user'] = username
            session.permanent = True
            app.permanent_session_lifetime = 3600
            return redirect("/")
        else:
            error = "Incorrect username and/or password"
            return render_template("login.html", error = error)

@app.route("/register", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("/signup.html")
    else:
        if request.form.get("password") == request.form.get("password2"):
            if database.newUser(request.form.get("login"), request.form.get("password")):
                return redirect("/")
            else:
                error = "Username has already been taken"
                return render_template("signup.html", error=error)
        else:
            error = "Passwords do not match"
            return render_template("signup.html", error=error)

@app.route("/logout")
def logout():
    del session['user']
    return redirect("/login")

@app.route("/post/<postid>", methods=["GET", "POST"])
def post(postid):
    if request.method == "GET":
        return render_template("/post.html", blogitem = database.getPost("rowid",postid)[0], comments = database.getComments("replyid",postid))
    else:#addComment(commentbody, commentid, postid, userid)
        if 'user' in session:
            database.addComment(request.form.get("comment_text"),0, postid, session['user'])
            return redirect("/post/" + postid)
        else:
            return redirect("/login")

@app.route("/makepost", methods=["GET", "POST"])
def makepost():
    if request.method == "GET":
        if 'user' in session:
            return render_template("/makepost.html")
        else:
            redirect("/login")
    else:
        form = request.form
        database.addPost(form.get("paragraph_text"), 0, session['user'])
        return redirect("/")

@app.route("/user")
def getuser():
    return redirect("/user/" + session['user'])

@app.route("/user/<userid>")
def profile(userid):
    print database.getPost("userid",userid)
    return render_template("profile.html", username = session['user'], blogitems = database.getPost("userid",userid), comments = database.getComments("userid",userid));

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gottacatch'emall"
    app.run()
