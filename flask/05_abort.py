#!/usr/bin/python3
#-*- coding: utf-8 -*-

# abort函数生成的相应，用于处理错误。
# 如果URL动态参数id对应的用户不存在，就返回状态码404


from flask import abort, Flask

app = Flask(__name__)

@app.route(r'/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

if __name__ == "__main__":
    app.run(debug = True)
