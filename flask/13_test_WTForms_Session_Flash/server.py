#! /usr/bin/python3 
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Length

app = Flask(__name__)
app.config ['SECRET_KEY'] = 'password' # 默认情况下，Flask-WTF能保护所有表单免受跨站请求伪造(CSRF)的攻击。
# 为了实心CSRF保护，Flask-WTF需要程序设置一个密钥。Flask-WTF使用这个密钥生成加密令牌，再用令牌验证请求中表单数据的真伪。

bootstrap = Bootstrap(app)

# 使用Flask-WTF时，每个web表单都有一个继承自Form的类表示。
# 这个类定义表单中的一组字段，每个字段都用对象表示。
# 字段对象可附属一个或者多个验证函数，验证函数用来验证用户提交的输入值是否符合要求。

class NameForm(Form):
    name = StringField('what is your name?', validators=[Required()]) # validators中是验证函数组成的列表
    password = PasswordField('what is your password?', validators=[Required(), Length(6)])
    submit = SubmitField('Submit')

@app.route(r'/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name') 
        old_password = session.get('password')
        if old_name is not None and old_name != form.name.data:
            flash('姓名不匹配')
        if old_name == form.name.data and old_password is not None and old_password != form.password.data:
            flash('密码错误')
        session['name'] = form.name.data # 将数据存储在session里
        session['password'] = form.password.data
        return redirect(url_for('index'))  # 使用重定向作为post请求的响应。响应的内容是URL，而不是包含HTML代码的字符串。
        # 浏览器收到这种响应时，会向重定向的URL发起GET请求，显示页面的内容。Post/重定向/Get模式
    return render_template('index.html', form=form, name=session.get('name'), password=session.get('password'))

if __name__ == "__main__":
    app.run(debug = True)
