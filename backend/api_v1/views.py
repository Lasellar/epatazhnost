from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import Item, Gig, ShoppingCart
from .serializers import (
    ItemSerializer, GigSerializer, ShoppingCartSerializer
)


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

    @action(
        detail=True, methods=('post', 'delete'),
        url_path='shopping-cart'
    )
    def shopping_cart(self, request, pk):
        """
        Добавляет товар в корзину или удаляет его из корзины.

        :param request: HTTP запрос.
        :param pk: ID товара.
        :return: Ответ с данными о товаре в корзине или статус удаления.
        """
        item = get_object_or_404(Item, id=pk).id
        user_cookie = request.headers['Cookie']
        if request.method == 'POST':
            serializer = ShoppingCartSerializer(
                data={'user_cookie': user_cookie, 'item': item},
                context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        if not ShoppingCart.objects.filter(
            user_cookie=user_cookie, item=item
        ).exists():
            return Response(
                {'error': 'Рецепта нет в списке покупок.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        ShoppingCart.objects.filter(
            user_cookie=user_cookie, item=item
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=('get',), url_path='get-shopping-cart')
    def get_shopping_cart(self, request):
        """
        Получает список товаров в корзине для текущего пользователя.

        :param request: HTTP запрос.
        :return: Ответ с данными о товарах в корзине.
        """
        user_cookie = request.headers['Cookie']
        queryset = ShoppingCart.objects.filter(user_cookie=user_cookie)
        serializer = ShoppingCartSerializer(
            queryset, context={'request': request}, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class GigViewSet(ReadOnlyModelViewSet):
    """
    ViewSet для управления концертами.
    Позволяет получать список концертов.
    """
    queryset = Gig.objects.filter(is_published=True)
    serializer_class = GigSerializer

