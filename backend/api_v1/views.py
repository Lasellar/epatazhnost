from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.generics import RetrieveAPIView

from .models import Item, Gig, ShoppingCart, MainPagePhoto
from .serializers import (
    ItemSerializer, GigSerializer
)
from bot_webhooks.utils import BOT


class ShopViewSet(ModelViewSet):
    """
    ViewSet для управления товарами в магазине.
    Позволяет получать список товаров и добавлять/удалять
    товары в корзину покупок.
    """
    queryset = Item.objects.filter(is_published=True)
    serializer_class = ItemSerializer
    pagination_class = None
    http_method_names = ('get', 'post')

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset, many=True, context={'request': request}
        )
        main_page_image = MainPagePhoto.objects.filter(
            is_published=True
        ).first().image.url
        return Response(
            {'main_page_image': main_page_image, 'items': serializer.data}
        )

    @action(detail=False, methods=('post',), url_path='create-order')
    def create_order(self, request):
        data = request.data
        return


class GigViewSet(ReadOnlyModelViewSet):
    """
    ViewSet для управления концертами.
    Позволяет получать список концертов.
    """
    queryset = Gig.objects.filter(is_published=True)
    serializer_class = GigSerializer
    pagination_class = None
