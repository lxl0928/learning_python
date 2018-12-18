#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route(r'/')
def index():
    return render_template('index.html')

@app.route(r'/user/<name>')
def user(name):
    return render_template('user.html', name = name)

if __name__ == "__main__":
    manager.run()
