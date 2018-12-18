#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 动态请求路由

from flask import Flask

app = Flask(__name__)

@app.route(r'/')
def index():
    return '<h1>hello world</h1>'

@app.route(r'/user/<name>')
def user(name):
    return '<h1>hello %s' % name

@app.route(r'/page/<id>')
def page(id):
    return '<h1> Page %d' % int(id)

if __name__ == "__main__":
    app.run(debug = True)
