import stripe
from django.conf import settings
from django.db import models

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(Products, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100), currency='rub')
        return stripe_product_price

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item

    @classmethod
    def create_or_update(cls, product_id, user):
        baskets = Basket.objects.filter(user=user, product_id=product_id)

        if not baskets.exists():
            obj = Basket.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated
