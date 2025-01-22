from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework.serializers import (
    ModelSerializer, ImageField, IntegerField, PrimaryKeyRelatedField,
    CharField, Serializer, SerializerMethodField, ValidationError,
    FloatField, BooleanField
)

from .models import (
    Category, Size, ItemSize, Item, ImageItem
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


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')


class ImageItemSerializer(ModelSerializer):
    class Meta:
        model = ImageItem
        fields = ('image',)


class SizeItemSerializer(ModelSerializer):
    name = CharField(source='size.name')

    class Meta:
        model = ItemSize
        fields = ('name', 'is_in_stock')


class ItemSerializer(ModelSerializer):
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


