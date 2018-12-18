#! /usr/bin/eny python3
# coding: utf-8

from django.conf.urls import url
from django.contrib import admin
from . import testdb
from . import view
from . import search, search2

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search$', search.search),
    url(r'^search_form$', search.search_form),
    url(r'^search_post$', search2.search_post),
    url(r'^admin/', admin.site.urls),
]
