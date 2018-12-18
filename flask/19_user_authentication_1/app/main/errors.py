from flask import render_template
from . import main
# 引入蓝本

@main.app_errorhandler(404) #蓝本中的错误处理程序，如果使用main.errorhandler修饰器，智能处理在蓝本中错误才触发处理程序，使用main.app_errorhandler()可以处理全局错误。
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
