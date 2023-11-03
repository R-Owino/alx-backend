#!/usr/bin/env python3
'''
A simple flask app that serves a template
'''
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    '''
    config class for babel
    '''
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


def get_user() -> Union[Dict, None]:
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


@babel.localeselector
def get_locale() -> str:
    ''' Gets specified locale for the web app '''
    # Check if 'locale' parameter is in the request and is a supported locale
    query_string = request.query_string.decode('utf-8')
    query_table = {
            key: value
            for key, value in (
                param.split('=') if '=' in param else (param, '')
                for param in query_string.split('&')
            )
        }
    if ('locale' in query_table and
       query_table['locale'] in app.config["LANGUAGES"]):
        return query_table['locale']

    # else get the best-matching language from request.accept_languages
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    '''
    Returns a string
    '''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
