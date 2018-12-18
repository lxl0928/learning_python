#a!/usr/bin/env python3
#-*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
from urllib.request import urlopen, quote

class HomeHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.render("home.html" )
    pass

class BillHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("bill.html")
    pass

def main():
    app = tornado.web.Application(
        [(r'/', HomeHandler), (r'/bill', BillHandler)],
        template_path = 'templates',
        static_path = 'static'
    )
    app.listen(8000)
    print("The server is running at http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()

if __name__  == '__main__':
    main()
