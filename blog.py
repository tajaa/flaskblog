from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = "root"

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


if __name__ == "__main__":
    app.run(debug=True)
