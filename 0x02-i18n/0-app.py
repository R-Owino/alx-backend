#!/usr/bin/env python3
'''
Simple flask app
'''

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', strict_slashes=False)

def index() -> str:
    ''' Returns a string '''
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)