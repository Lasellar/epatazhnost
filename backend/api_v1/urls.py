from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ShopViewSet

router = DefaultRouter()
router.register('shop', ShopViewSet, basename='shop')


urlpatterns = [
    path('', include(router.urls))
]

