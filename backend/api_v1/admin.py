from django.conf import settings
from django.contrib.admin import (
    ModelAdmin, register,
)

from .models import (
    Category, Size, ItemSize, Item, ImageItem
)


class CustomModelAdmin(ModelAdmin):
    empty_value_display = settings.EMPTY_VALUE


@register(Category)
class CategoryAdmin(CustomModelAdmin):
    list_display = ('id', 'name', 'slug')


@register(Size)
class SizeAdmin(CustomModelAdmin):
    list_display = ('id', 'name')


@register(ItemSize)
class ItemSizeAdmin(CustomModelAdmin):
    list_display = ('id', 'item', 'size')


@register(Item)
class ItemAdmin(CustomModelAdmin):
    list_display = ('id', 'name', 'is_published')


@register(ImageItem)
class ImageItemAdmin(CustomModelAdmin):
    list_display = ('id', 'image', 'item', 'is_published')
