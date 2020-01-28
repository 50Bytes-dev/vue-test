from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import *

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class PostViewSet(viewsets.ModelViewSet):
    """
    API конечная точка для Постов для редактирования и т.д.
    """
    queryset = Post.objects.prefetch_related('photos').all()
    serializer_class = PostSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API конечная точка для Фото для редактирования и т.д.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
