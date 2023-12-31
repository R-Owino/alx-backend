#!/usr/bin/env python3
''' A simple app that serves a template '''

from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    ''' Config class for babel '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    '''
    Checks URL for locale parameter, and forces the Locale of the app
    '''
    # check if locale parameter is in the URL
    if request.args.get('locale'):
        return request.args.get('locale')

    # otherwise return the best match with our supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    ''' Returns a user dictionary or None if the ID cannot be found '''
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    ''' Finds a user if any, and set it as a global on flask.g.user '''
    user = get_user()
    if user:
        g.user = user


@app.route('/')
def index() -> str:
    ''' Returns a string '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
