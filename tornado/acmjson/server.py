#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
from urllib.request import urlopen
import json

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        data = json.loads(self.get_json_data())
        self.render("index.html", datas = data)

    def get_json_data(self):
        url = "http://contests.acmicpc.info/contests.json"
        return urlopen(url).read().decode()

class OtherIndex(tornado.web.RequestHandler):

    def get(self):
        data = json.loads(self.get_json_data())
        self.render("other.html", datas = data)

    def get_json_data(self):
        url = "https://api.douban.com/v2/user?q=jzqt"
        return urlopen(url).read().decode()

def main():
    app = tornado.web.Application(
        [(r'/', IndexHandler), (r'/other', OtherIndex)],
        template_path = 'templates'
    )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
