#!/usr/bin/env python3
'''
A simple flask app that serves a template
'''
from flask_babel import Babel
from flask import Flask, render_template, request


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


@babel.localeselector
def get_locale() -> str:
    '''  '''
    # Check if 'locale' parameter is in the request and is a supported locale
    if ('locale' in request.args and
       request.args['locale'] in app.config['LANGUAGES']):
        return request.args['locale']

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
