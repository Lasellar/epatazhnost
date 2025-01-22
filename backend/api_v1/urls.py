from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ShopViewSet, GigViewSet

router = DefaultRouter()
router.register('shop', ShopViewSet, basename='shop')
router.register('concerts', GigViewSet, basename='concerts')


urlpatterns = [
    path('', include(router.urls))
]

