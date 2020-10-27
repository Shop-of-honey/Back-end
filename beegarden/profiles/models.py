from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import EmailField
from phone_field import PhoneField


class User(AbstractUser):
    phone = PhoneField(null=False, blank=False, unique=True, help_text='Contact phone number')
    email = EmailField(max_length=100, help_text='Email')

    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Назание товара', max_length=255,
                            help_text='Название товара длиной не больше 255 символов')
    description = models.CharField('Описание товара', max_length=1023,
                                   help_text='Описание товара может быть максимум в 1023 символов',
                                   null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Создатель',
                                related_name='created_products', null=True)
    price = models.PositiveIntegerField(help_text='the price of the product')

    class Meta:
        db_table = 'Product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
