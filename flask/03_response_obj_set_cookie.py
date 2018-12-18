#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, make_response

app = Flask(__name__)

@app.route(r'/')
def index():
    response = make_response('<h1> This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__ == "__main__":
    app.run(debug = True)
