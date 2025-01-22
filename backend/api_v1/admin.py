from django.conf import settings
from django.contrib.admin import (
    ModelAdmin, register, TabularInline
)

from .models import (
    Category, Size, ItemSize, Item, ImageItem
)


class CustomModelAdmin(ModelAdmin):
    empty_value_display = settings.EMPTY_VALUE


class SizeInline(TabularInline):
    model = ItemSize
    extra = 0


class ImageInline(TabularInline):
    model = ImageItem
    extra = 0


@register(Category)
class CategoryAdmin(CustomModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


@register(Size)
class SizeAdmin(CustomModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@register(Item)
class ItemAdmin(CustomModelAdmin):
    inlines = (SizeInline, ImageInline)
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('name',)
    list_editable = ('is_published', )
