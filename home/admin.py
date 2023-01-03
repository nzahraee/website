from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update')
    list_filter = ('create',)



class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'create','update','amount','available','unite_price','discount','total_price','total_price',]
    list_filter = ('available',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(product, productAdmin)

