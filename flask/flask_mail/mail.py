#! /usr/bin/env python3
# coding: utf-8 

from flask import Flask
from flask_mail import Mail, Message 
from threading import Thread
import os

app = Flask(__name__)

app.config["MAIL_SERVER"] = 'smtp.qq.com'
app.config["MAIL_PORT"] = 25
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME") or "test@test.com"
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD") or "password@test.com"

mail = Mail(app)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route("/sync")
def send_email():
    msg = Message("Hi", sender=app.config["MAIL_USERNAME"],
            recipients=["757580264@qq.com"])
    msg.html = "<b>send email asynchronously</b>"

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return "Send Successfully"

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
pass

