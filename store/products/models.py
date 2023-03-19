from django.db import models
from unicodedata import category


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField("Имя", max_length=256, unique=True)
    description = models.TextField("Описание", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField("Имя", max_length=256)
    image = models.ImageField("Изображение", upload_to='products_images', null=True, blank=True)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=0)
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey(to=ProductCategory, verbose_name="Категория", on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
