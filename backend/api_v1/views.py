from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Item, Gig
from .serializers import (
    ItemSerializer, GigSerializer
)


class ShopViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.filter(is_published=True)
    serializer_class = ItemSerializer
    # pagination_class = None


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
