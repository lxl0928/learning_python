#! /usr/bin/env python3
# coding: utf-8
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

class EntryHandler(tornado.web.RequestHandler):
    def get(self, slug=None):
        if slug:
            self.write("The URL is: ", self.request.uri)
        else:
            self.write("The URL is: ", self.request.uri)

class Entry2015Handler(tornado.web.RequestHandler):
    def get(self, slug=None):
        if slug:
            self.write("The URL is: ", self.request.uri)
        else:
            raise tornado.web.HTTPError(404)

class DetailHandler(tornado.web.RequestHandler):
    def get(self, year, month, day, slug=None):
        if slug:
            self.write("The URL is: ", self.request.uri)
        else:
            raise torndo.web.HTTPError(404)
