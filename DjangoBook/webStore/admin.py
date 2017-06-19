#coding:utf8
from django.contrib import admin

# Register your models here.

from webStore.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','image')

admin.site.register(Product,ProductAdmin)
