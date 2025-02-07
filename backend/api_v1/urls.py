from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ShopViewSet, GigViewSet, send_message_by_bot

app_name = 'api_v1'
router = DefaultRouter()
router.register('shop', ShopViewSet, basename='shop')
router.register('concerts', GigViewSet, basename='concerts')


urlpatterns = [
    path('', include(router.urls)),
    path(
        'send_message_by_bot/<str:chat_id>/<str:text>/',
        send_message_by_bot, name='send_message_by_bot'
    ),
]

