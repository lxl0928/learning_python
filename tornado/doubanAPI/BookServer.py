#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json
import tornado.web
import tornado.ioloop
from urllib.request import urlopen, quote

class BookHandler(tornado.web.RequestHandler):

    def get(self):
        text = self.get_query_argument("q", None)
        print(text)
        if text is None:
            self.render("book.html", books=None)
        else:
            data = json.loads(self.get_json_data(text))
            self.render("book.html", books=data["books"])

    def get_json_data(self, text):
        url = "https://api.douban.com/v2/book/search?count=100&q={}".format(quote(text))
        return urlopen(url).read().decode()

def main():
    app = tornado.web.Application(
        [(r'/', BookHandler)],
        template_path = "templates"
    )
    app.listen(8001)
    print("The server is running at http://localhost:8001")
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
