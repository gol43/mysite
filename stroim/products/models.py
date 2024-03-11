from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField()
    cost = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='products/',
        blank=True
    )
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shopping_cart')

    def __str__(self):
        return f'{self.user} добавил "{self.product}" в список покупок'


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='comments')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',)

    text = models.TextField(
        max_length=200,)

    created = models.DateTimeField(
        verbose_name='Дата коммента',
        auto_now_add=True,)
    def __str__(self):
        return self.text