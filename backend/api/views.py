from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer, Comment, CommentSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        _queryset = self.queryset
        message_id = self.request.GET.get('message_id')
        if message_id:
            message_id = int(message_id)
            _queryset = _queryset.filter(message__id=message_id)
        return _queryset


