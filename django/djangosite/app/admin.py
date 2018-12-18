from django.contrib import admin
from app.models import Moment, Account, Contact
# Register your models here.
admin.site.register([Moment, Account, Contact])
