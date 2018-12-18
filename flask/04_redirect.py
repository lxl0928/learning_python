#/usr/bin/python3
# -*- coding: utf-8 -*-

# 重定向相应类型，该相应没有页面，只告诉浏览器一个新地址用以加载新页面。一般用于web表单。

from flask import Flask, redirect

app = Flask(__name__)

@app.route(r'/')
def index():
    return redirect('http://www.timilong.com')

if __name__ == "__main__":
    app.run(debug = True)
