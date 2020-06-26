#!/usr/bin/python3

import os
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return("Hello World!")

if __name__ == '__main__':
    app.run(host="localhost", port=os.environ.get('PORT'), debug=True)

