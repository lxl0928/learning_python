from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager

bootstrap = Bootstrap() # 使用bootstrap框架渲染模板
mail = Mail() # 使用邮件扩展
moment = Moment() # 使用moment.js是轻量级的js日期处理类库。集成moment.js到Jinja2模板的集成
db = SQLAlchemy() # flask数据库管理扩展包

login_manager = LoginManager() # 使用Flask-Login认证用户
login_manager.session_protection = 'strong' # session_protection属性可以设为None, basic, strong.其中strong会验证用户代理信息和IP地址，发现异常登出用户。

login_manager.login_view = 'auth.login' # login_view属性设置登录页面的端点


def create_app(config_name): # 创建应用, 程序的工厂函数，收一个参数，是程序所使用的配置名。
    app = Flask(__name__)
    app.config.from_object(config[config_name]) #配置类在config.py中定义。其中的配置可以使用Flask app.config配置对象提供的from_object()方法直接导入程序。

    config[config_name].init_app(app) # 配置对象，通过名字在config字典中选择。
#程序创建并配置好后，就可以初始化扩展了。
    
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) # 将蓝本在主程序中注册

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app # 工厂函数返回创建的程序实例

