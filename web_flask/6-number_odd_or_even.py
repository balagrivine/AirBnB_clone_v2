#!/usr/bin/python3
"""Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition
"""


from flask import Flask, render_template
from markupsafe import escape

#create an instance of Flask class
app = Flask(__name__)

#define the route decorator to det which function to call for a page
@app.route("/", strict_slashes=False)
def hello():
    """Function to call for the / page"""
    return "Hello HBNB!"

#define function to be called for the page /hbnb
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function to be called for the page /hbnb"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def hbnb_text(text):
    """function to be called for the page /hbnb/<text>"""
    formatted = text.replace('_', ' ')
    return "C {}".format(formatted)

@app.route("/python/<text>", strict_slashes=False)
def python_text(default="text"):
    """function to be rendered for the page /hbnb/python/<text>"""
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """function to display for page /number/<n>"""
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def return_template(n):
    """function to call for /number_template/<n>"""
    return render_template("5-number.html", number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=True)
def number_odd_or_even(n):
    """function to render for page /number_odd_or_even/<n>"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
