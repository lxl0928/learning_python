#!/usr/bin/python3 
# -*- coding: utf-8 -*-

from flask import Flask 

app = Flask(__name__)
@app.route(r'/')
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run()
