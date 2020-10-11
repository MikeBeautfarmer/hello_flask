from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "WILLKOMMEN!"
    aktuelles_jahr = datetime.datetime.now().year

    countries = ["Österreich", "Deutschland", "Schweiz", "Liechtenstein"]
    return render_template("index.html",
                           some_text=some_text,
                           aktuelles_jahr=aktuelles_jahr,
                           countries=countries)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
