import datetime

from flask import Flask, render_template, request, make_response

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


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html")
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)
        return response


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
