#!/usr/bin/env python3
'''
Simple flask app that serves a template
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# config class with languages attribute
class Config(object):
    ''' config class for babel '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale() -> str:
    '''
    Checks URL for locale parameter, and forces the Locale of the app
    '''
    # Check if the 'locale' parameter is in the request and
    # is a supported locale
    if request_locale in Config.LANGUAGES:
        return request_locale

    # else gets the best-matching language from request.accept_languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    ''' Returns a user dictionary or None if the ID cannot be found '''
    request_user = request.args.get('login_as')

    if request_user:
        return users.get(int(request_user))
    return None


@app.before_request
def before_request():
    ''' Finds a user if any, and set it as a global on flask.g.user '''
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Returns a string '''
    return render_template('5-index.html')


if __name__ == "__main__":
    app.config.from_object(Config)
    app.run(host="localhost", port=5000, debug=True)
