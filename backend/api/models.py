from datetime import datetime

from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now)

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'date', 'pk')


#############################################################################


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='comments')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'text', 'date', 'message', 'pk')
