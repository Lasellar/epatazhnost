from django.conf import settings
from django.contrib.admin import (
    ModelAdmin, register, TabularInline
)

from .models import (
    Category, Size, ItemSize, Item, ImageItem, Gig, ShoppingCart
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
    list_display = ('id', 'is_published', 'name')
    list_display_links = ('name',)
    list_editable = ('is_published', )


@register(Gig)
class GigAdmin(CustomModelAdmin):
    list_display = (
        'is_published', 'city', 'date', 'time', 'place', 'price'
    )
    list_display_links = ('city',)
    list_editable = ('is_published', 'price',)


@register(ShoppingCart)
class ShoppingCartAdmin(CustomModelAdmin):
    list_display = ('user_cookie', 'item')
