#!/usr/bin/env python3
'''
Simple flask app that serves a template
'''

from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


# config class with languages attribute
class Config(object):
    ''' config class for babel '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale() -> str:
    # Determine the best-matching language from request.accept_languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Returns a string '''
    return render_template('2-index.html')


if __name__ == "__main__":
    app.config.from_object(Config)
    app.run(host="localhost", port=5000, debug=True)
