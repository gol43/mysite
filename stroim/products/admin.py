from django.contrib import admin

from django.contrib import admin

from .models import Product, Category, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)