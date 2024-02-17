#!/usr/bin/python3
"""start a flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Function to be rendered for the page /states_list"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown():
    """Function to be called to close the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host=0.0.0.0, port=5000)
