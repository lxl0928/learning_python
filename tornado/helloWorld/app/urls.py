#! /usr/bin/env python3 
# coding: utf-8

from app.main import *
import tornado.web
import tornado.ioloop

def make_app():
    handlers_url = [(r"/", MainHandler),
        (r"/entry/2015", Entry2015Handler),
        (r"/entry/([^/]*)", EntryHandler),
        (r"/entry/(\d{4})/(\d{2})/(\d{2})/([a-zA-Z\-0-9\.:,_]+)/?", DetailHandler),
    ]
    return tornado.web.Application(handlers_url)
