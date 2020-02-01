from django.db.models import Prefetch
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import *
from .serializers import *

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class PostViewSet(viewsets.ModelViewSet):
    """
    API конечная точка для Постов для редактирования и т.д.
    """
    queryset = Post.objects.prefetch_related(Prefetch(
        'photos', queryset=Photo.objects.prefetch_related('sizes').all()
    )).all()
    serializer_class = PostSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API конечная точка для Фото для редактирования и т.д.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API конечная точка для Фото для редактирования и т.д.
    """
    queryset = Product.objects.select_related('post').prefetch_related('post__photos__sizes').all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductGetSerializer
        if self.action == 'retrieve':
            return ProductGetSerializer
        return ProductPostSerializer  # create/destroy/update.