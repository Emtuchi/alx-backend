#!/usr/bin/env python3
"""Basic route task 1"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

@app.route('/', methods=["GET"], strict_slashes=False)
def home():
    """ Home page """
    return render_template('1-index.html')

class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")