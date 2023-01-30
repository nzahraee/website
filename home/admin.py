from django.contrib import admin
from .models import *


class productVariantInlines(admin.TabularInline):
    model = Variants
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','sub_category')
    list_filter = ('create',)
    prepopulated_fields = {
        'slug':('name',)
    }

class variantAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

class sizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

class colorAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

class productAdmin(admin.ModelAdmin):
    list_display = ['name','create','update','amount','available','unite_price','discount','total_price',]
    list_filter = ('available',)
    list_editable = ('amount',)
    raw_id_fields = ('category',)
    inlines = [productVariantInlines]


admin.site.register(Category, CategoryAdmin)
admin.site.register(product, productAdmin)
admin.site.register(Variants,variantAdmin)
admin.site.register(size,sizeAdmin)
admin.site.register(color, colorAdmin)
