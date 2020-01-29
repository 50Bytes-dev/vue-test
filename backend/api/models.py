from datetime import datetime

import vk
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


class Photo(models.Model):
    """sizes* text* post*"""
    photo_id = models.BigIntegerField()
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')
    # sizes - from Size


class Size(models.Model):
    """photo* type* url* width* height*"""
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='sizes')
    type = models.CharField(max_length=1)
    url = models.URLField()
    width = models.CharField(max_length=5)
    height = models.CharField(max_length=5)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    date_post = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Post
        fields = '__all__'
