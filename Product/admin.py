from django.contrib import admin
# Register your models here.
from Product.models import Product
from Product.models import Category

admin.site.register(Product)
admin.site.register(Category)
