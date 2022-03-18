from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'type']


class AdminCategory(admin.ModelAdmin):
    list_display = ['types']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
