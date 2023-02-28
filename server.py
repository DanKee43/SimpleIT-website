from flask import Flask, render_template, json

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("base.html")


@app.errorhandler(404)
def error404_page(e):
    return render_template("404_page.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
