#! /usr/bin/env python3
# coding: utf-8 

import tornado.web
import tornado.ioloop
from app.urls import make_app

def main():
    app = make_app()
    app.listen(8888)
    print("The server is running at http://127.0.0.1:8888")
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
