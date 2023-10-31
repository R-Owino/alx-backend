#!/usr/bin/env python3
'''
Simple flask app that serves a template
'''

from flask import Flask, render_template, request
from flask_babel import _,  Babel
app = Flask(__name__)
babel = Babel(app)


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
    return render_template('4-index.html')


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


if __name__ == "__main__":
    app.config.from_object(Config)
    app.run(host="localhost", port=5000, debug=True)
