#a!/usr/bin/env python3
#-*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
from urllib.request import urlopen, quote
import json

class UserHandler(tornado.web.RequestHandler):

    def get(self):
        text = self.get_query_argument("q", None)
        print(text)
        if text is None:
            self.render("user.html", users=None)
        else:
            data = json.loads(self.get_json_data(text))
            self.render("user.html", users=data["users"])

    def get_json_data(self, text):
        url = "https://api.douban.com/v2/user?count=100&q={}".format(quote(text))
        return urlopen(url).read().decode()


def main():
    app = tornado.web.Application(
        [(r'/', UserHandler)],
        template_path = 'templates'
    )
    app.listen(8000)
    print("The server is running at http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()

if __name__  == '__main__':
    main()
