from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework.serializers import (
    ModelSerializer, ImageField, IntegerField, PrimaryKeyRelatedField,
    CharField, Serializer, SerializerMethodField, ValidationError,
    FloatField, BooleanField
)

from .models import (
    Category, Size, ItemSize, Item, ImageItem, Gig, ShoppingCart, UserInfo
)

import base64


class Base64ImageField(ImageField):
    """
    Поле для хранения изображений в формате base64.
    """
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            fmt, imgstr = data.split(';base64,')
            ext = fmt.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class SizeItemSerializer(ModelSerializer):
    """Сериализатор для поля размеров у вещи."""
    name = CharField(source='size.name')

    class Meta:
        model = ItemSize
        fields = ('name', 'is_in_stock')


class ItemSerializer(ModelSerializer):
    """Сериализатор для вещи."""
    sizes = SizeItemSerializer(source='itemsize', many=True)
    attachments = SerializerMethodField()
    main_image = SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            'id', 'is_published', 'name', 'price', 'description', 'sizes',
            'main_image', 'attachments'
        )

    def get_attachments(self, obj):
        return [image_item.image.url for image_item in obj.imageitem.all()]

    def get_main_image(self, obj):
        return obj.main_image.url


class GigSerializer(ModelSerializer):
    """Сериализатор для концерта."""
    image = SerializerMethodField()

    class Meta:
        model = Gig
        fields = (
            'city', 'image', 'date', 'time', 'place', 'price', 'tickets_url'
        )

    def get_image(self, obj):
        return obj.image.url


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        firelds = (
            'id', 'cookie', 'first_name', 'last_name',
            'third_name', 'telegram', 'sdek'
        )


class OrderSerializer(ModelSerializer):
    class Meta:
        model = ItemSize
        fields = (
            'id', 'user', 'items'
        )


