#!/usr/bin/python3
"""Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition
"""


from flask import Flask

#create an instance of Flask class
app = Flask(__name__)

#define the route decorator to det which function to call for a page
@app.route("/", strict_slashes=False)
def hello():
    """Function to call for the / page"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
