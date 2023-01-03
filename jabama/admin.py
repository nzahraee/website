from django.contrib import admin
from .models import *


class acomodationAdmin(admin.ModelAdmin):
   list_display = ['name','create','update','avail','desc','price','discount',]


admin.site.register(acomodation, acomodationAdmin)
