from django.shortcuts import render
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
