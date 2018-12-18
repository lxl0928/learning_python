#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route(r'/')
def index():
    return render_template('index.html')

@app.route(r'/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug = True)
