#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from datetime import datetime
from flask.ext.moment import Moment

app =Flask(__name__)
moment = Moment(app)

@app.route(r'/')
def index():
    return render_template('index.html', current_time = datetime.utcnow())

if __name__ == "__main__":
    app.run(debug = True)
