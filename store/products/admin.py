from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductCategory, Products, Basket


# Register your models here.
@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    readonly_fields = ("get_image", 'description',)
    fields = ('name', 'get_image', 'description', ('price', 'quantity'),
              'stripe_product_price_id', 'category', 'image',)
    search_fields = ('name',)
    ordering = ('-name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Внешний вид"


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0


admin.site.site_title = "StoreBD"
admin.site.site_header = "StoreBD"
