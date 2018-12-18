#! /usr/bin/python3

# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, flash
from . import auth #当前模块中引入蓝本，然后使用蓝本的route修饰器定义与认证相关的路由。
from flask.ext.login import login_user
from ..models import User
from .forms import LoginForm

@auth.route(r'/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # 视图函数login创建了一个LoginForm的实例对象，当请求类型是get时候，视图函数直接渲染模板，即显示表单。当表单在POST请求中提交的时候，Flask-WTF中的validate_on_submit()函数会验证表单数据，然后尝试登入用户。

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # 数据库中加载用户。
        if user is not None and user.verify_password(form.password.data): # 用户存在并密码匹配
            login_user(user, form.remember_me.data) # 调用Flask-Login中的login_user()函数，在用户会话中把用户标记为已登录。login_user()函数，的参数是要登录的用户，以及可选的“记住我”的布尔值，“记住我”在表单中填写，如果是False，则关闭浏览器后会话就过期了，下次需要重新登录。如果值为True, 那么会在用户浏览器中写入一个长期有效的cookie,使用这个cookie可以复现用户会话。

            return redirect(request.args.get('next') or url_for('main.index'))
# 提交登录密令的POST请求最后也做了重定向，不过目标URL有两种可能。用户访问没有授权的URL时会显示登录表单，Flask-Login会把原地址保存在查询字符串的next参数中，这个参数可以从request.args字典中读取。如果查询字符串没有next参数，则重定向到首页。
        flash('Invalid username or password') # 密码不匹配, flash一个新的提示消息
    return render_template('auth/login.html', form=form) #Flask认为模板的路径是相对于程序模板文件夹而言的。
#render_template()函数会首先搜索程序的配置的模板文件夹， #Flask认为膜纳米容纳后再搜索蓝本配置的模板文件夹。

