from flask import Flask, render_template

from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "8f2f260684695eb8fce48a35302dd139"

posts = [
    {
        "author": "John Foe",
        "title": "Blog Post 1",
        "content": "First post conent",
        "date_posted": "April 20, 2023",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "First post conent",
        "date_posted": "February 20, 2023",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About Us")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
