from django.contrib import admin

from django.contrib import admin

from .models import Product, Category, Comment, ShoppingCart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ShoppingCart)