from django.db.models import (
    Model, CharField, IntegerField, ForeignKey, BooleanField,
    ManyToManyField, SlugField, TextField, CASCADE, ImageField
)


class Category(Model):
    name = CharField(max_length=30, unique=True)
    slug = SlugField(max_length=50, unique=True)


class Size(Model):
    name = CharField(max_length=10, unique=True)


class Item(Model):
    name = CharField(max_length=64)
    description = TextField()
    sizes = ManyToManyField(Size, related_name='itemsizes', through='ItemSize')
    is_published = BooleanField(blank=True, default=False)
    main_image = ImageField(upload_to='items_images')


class ItemSize(Model):
    item = ForeignKey(Item, on_delete=CASCADE, related_name='itemsize')
    size = ForeignKey(Size, on_delete=CASCADE, related_name='itemsize')
    is_in_stock = BooleanField(default=False, null=True, blank=True)


class ImageItem(Model):
    image = ImageField(upload_to='items_images')
    item = ForeignKey(
        Item, related_name='imageitem', on_delete=CASCADE
    )
    is_published = BooleanField(blank=True, default=False)
