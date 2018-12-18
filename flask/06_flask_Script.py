#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Flask-Script是一个Flask扩展，为Flask程序添加了一个命令行解析器。

from flask import Flask
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route(r'/')
def index():
    return '<h1> hello , world</h1>'

if __name__ == "__main__":
    manager.run()
