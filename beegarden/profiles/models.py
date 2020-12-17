from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from django.db.models import EmailField
from phone_field import PhoneField


class User(AbstractUser):
    phone = PhoneField(null=True, blank=True, unique=False, help_text='Contact phone number')
    email = EmailField(max_length=100, help_text='Email')

    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Comment(models.Model):
    text = models.TextField('Текст комментария', max_length=1023)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    datetime_create = models.DateTimeField('Дата создания', auto_now=True)

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


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
    location = models.CharField('Местоположение продавца', max_length=1023,
                                   help_text='Местоположение продавца может быть максимум в 1023 символов',
                                   null=True, blank=True)
    comment = GenericRelation(Comment)

    class Meta:
        db_table = 'Product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
