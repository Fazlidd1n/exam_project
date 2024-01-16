from django.contrib import admin

from apps.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    pass