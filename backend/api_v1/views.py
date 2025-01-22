from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Item
from .serializers import (
    ItemSerializer
)


class ShopViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.filter(is_published=True)
    serializer_class = ItemSerializer
    # pagination_class = None

