from django.contrib import admin
from .models import *


class acomodationAdmin(admin.ModelAdmin):
   list_display = ['name']


admin.site.register(acomodation, acomodationAdmin)
