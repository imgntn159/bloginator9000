from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "HOME PAGE"

@app.route("/about")
def about():
    return "ABOUT PAGE"

@app.route("/login")
def login():
    return "LOGIN PAGE"

@app.route("/logout")
def logout():
    return "LOGOUT PAGE"

@app.route("/post")
def post():
    return "INDIVIDUAL POST"

if __name__ == "__main__":
        app.run()
