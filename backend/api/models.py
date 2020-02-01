from datetime import datetime

import vk
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import BrinIndex
from django.db import models, transaction
from django.utils import timezone
from rest_framework import serializers


class Post(models.Model):
    """post_id* from_id* owner_id* date_post* text* date_created"""
    post_id = models.BigIntegerField()
    from_id = models.BigIntegerField()
    owner_id = models.BigIntegerField()
    date_post = models.DateTimeField()
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    # photos - from Photo
    # products - from Product


class Photo(models.Model):
    """photo_id* sizes* text* post*"""
    photo_id = models.BigIntegerField()
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')
    # sizes - from Size

    class Meta:
        indexes = (
            BrinIndex(fields=['id']),
        )


class Size(models.Model):
    """photo* type* url* width* height*"""
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='sizes')
    type = models.CharField(max_length=1)
    url = models.URLField()
    width = models.CharField(max_length=5)
    height = models.CharField(max_length=5)

    class Meta:
        indexes = (
            BrinIndex(fields=['photo']),
        )


class Product(models.Model):
    """title photo* price_trade* price* percent description* sizes* places* categories*"""
    title = models.CharField(max_length=300, default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='products')
    price_trade = models.BigIntegerField()
    price = models.BigIntegerField()
    percent = models.PositiveIntegerField(default=0)
    description = models.TextField()
    sizes = ArrayField(models.CharField(max_length=80, verbose_name='Размер'), size=100, verbose_name='Размеры')
    places = ArrayField(models.CharField(max_length=80, verbose_name='Место'), size=100, verbose_name='Места')
    categories = ArrayField(models.CharField(max_length=80, verbose_name='Категория'), size=100, verbose_name='Категории')
