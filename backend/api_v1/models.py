from django.db.models import (
    Model, CharField, IntegerField, ForeignKey, BooleanField,
    ManyToManyField, SlugField, TextField, CASCADE, ImageField
)


class Category(Model):
    name = CharField(max_length=30, unique=True)
    slug = SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Size(Model):
    name = CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Item(Model):
    name = CharField(max_length=64)
    description = TextField()
    sizes = ManyToManyField(Size, related_name='itemsizes', through='ItemSize')
    is_published = BooleanField(blank=True, default=False)
    main_image = ImageField(upload_to='items_images')

    class Meta:
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'

    def __str__(self):
        return self.name


class ItemSize(Model):
    item = ForeignKey(Item, on_delete=CASCADE, related_name='itemsize')
    size = ForeignKey(Size, on_delete=CASCADE, related_name='itemsize')
    is_in_stock = BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Вещь-размер'
        verbose_name_plural = 'Вещь-размер'

    def __str__(self):
        return f'{self.item}-{self.size}-{self.is_in_stock}'


class ImageItem(Model):
    image = ImageField(upload_to='items_images')
    item = ForeignKey(
        Item, related_name='imageitem', on_delete=CASCADE
    )
    is_published = BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = 'Вещь-доп.фото'
        verbose_name_plural = 'Вещь-доп.фото'

    def __str__(self):
        return f'{self.item}-{self.image}-{self.is_published}'
