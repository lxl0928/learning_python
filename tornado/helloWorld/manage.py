#! /usr/bin/env python3
# coding: utf-8

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application(
        [(r"/", MainHandler)],
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8111)
    print("The server is running at http://127.0.0.1:8111")
    tornado.ioloop.IOLoop.current().start()
