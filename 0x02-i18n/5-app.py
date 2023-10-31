#!/usr/bin/env python3
'''
Simple flask app that serves a template
'''

from flask import Flask, render_template, request, g
from flask_babel import _,  Babel
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


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Returns a string '''
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('5-index.html')


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


def get_user():
    ''' Returns a user dictionary or None if the ID cannot be found '''
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    ''' Finds a user if any, and set it as a global on flask.g.user '''
    user = get_user()
    if user:
        g.user = user


if __name__ == "__main__":
    app.config.from_object(Config)
    app.run(host="localhost", port=5000, debug=True)
