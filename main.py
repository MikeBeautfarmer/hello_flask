from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Nachricht von Handler!".replace("Handler", "Flask Applikation")
    datum = datetime.datetime.now()

    countries = ["Österreich", "Deutschland", "Schweiz", "Liechtenstein"]
    return render_template("index.html",
                           some_text=some_text,
                           datum=datum,
                           countries=countries)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
