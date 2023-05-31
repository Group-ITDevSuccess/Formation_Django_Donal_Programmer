from django.contrib import admin

from .models import Products
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'description']
    
                         
admin.site.register(Products, AdminProduct)
