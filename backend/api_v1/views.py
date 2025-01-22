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
        user_cookie = request.headers['Cookie']
        queryset = ShoppingCart.objects.filter(user_cookie=user_cookie)
        serializer = ShoppingCartSerializer(
            queryset, context={'request': request}, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class GigViewSet(ReadOnlyModelViewSet):
    queryset = Gig.objects.filter(is_published=True)
    serializer_class = GigSerializer


@api_view(['GET'])
def get_request_obj(request):
    user_cookie = request.headers['Cookie']
    return Response(
        {
            'ip': request.META.get(
                'HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR')
            ),
            'cookie': user_cookie,
            'headers': dict(request.headers),
        }, status=status.HTTP_200_OK
    )
