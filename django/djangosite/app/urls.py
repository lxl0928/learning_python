#! /usr/bin/env python3
# coding: utf-8

from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'moments_input', views.moments_input),
    url(r'', views.welcome),
]
