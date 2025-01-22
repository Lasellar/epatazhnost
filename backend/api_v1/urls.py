from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ShopViewSet, GigViewSet, get_request_obj

router = DefaultRouter()
router.register('shop', ShopViewSet, basename='shop')
router.register('concerts', GigViewSet, basename='concerts')


urlpatterns = [
    path('get_request/', get_request_obj, name='g_r'),
    path('', include(router.urls))
]

