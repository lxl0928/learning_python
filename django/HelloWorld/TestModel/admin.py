#! /usr/bin/eny python3
# coding: utf-8

from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
