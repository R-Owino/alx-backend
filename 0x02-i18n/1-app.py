#!/usr/bin/env python3
'''
Simple flask app that serves a template
'''

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


# config class with languages attribute
class Config(object):
    ''' config class for babel '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# initialize babel object
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Returns a string '''
    return render_template('1-index.html')


if __name__ == "__main__":
    app.config.from_object(Config)
    app.run(host="localhost", port=5000, debug=True)
