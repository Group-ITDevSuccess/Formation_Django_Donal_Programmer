from django.contrib import admin

from .models import Products
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'description']
    list_editable = ['available']
                         
admin.site.register(Products, AdminProduct)
