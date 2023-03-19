from django.contrib import admin

from .models import ProductCategory, Products


# Register your models here.
@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_display_links = ("name",)
    list_filter = ("category",)
    search_fields = ("name", "category")


admin.site.site_title = "StoreBD"
admin.site.site_header = "StoreBD"
