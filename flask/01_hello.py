#!/usr/bin/python3 
# -*- coding: utf-8 -*-

# 测试flask web开发

from flask import Flask 

app = Flask(__name__)

@app.route(r'/')
def index():
    return '<h1> hello world </h1>'

if __name__ == "__main__":
    app.run(debug=True)
