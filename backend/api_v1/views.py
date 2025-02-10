from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import Item, Gig, ShoppingCart
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
    # pagination_class = None
    http_method_names = ('get', 'post')

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=('post',), url_path='create-order')
    def create_order(self, request):
        data = request.data
        user_cookie = data.get('cookie')
        promo = data.get('promocode')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        third_name = data.get('third_name')
        tg = data.get('telegram')
        sdek = data.get('sdek')
        items = data.get('items')
        return


class GigViewSet(ReadOnlyModelViewSet):
    """
    ViewSet для управления концертами.
    Позволяет получать список концертов.
    """
    queryset = Gig.objects.filter(is_published=True)
    serializer_class = GigSerializer


@api_view(['GET'])
def send_message_by_bot(request, chat_id, text):
    if request.user.is_superuser:
        BOT.send_text(chat=chat_id, text=text)
        return Response(data={'status': 'Отправлено!'}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

