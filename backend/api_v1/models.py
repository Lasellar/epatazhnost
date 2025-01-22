from django.db.models import (
    Model, CharField, IntegerField, ForeignKey, BooleanField,
    ManyToManyField, SlugField, TextField, CASCADE, ImageField, UniqueConstraint
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
    category = ForeignKey(
        Category, on_delete=CASCADE, related_name='itemcategory'
    )
    price = IntegerField()

    class Meta:
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'

    def __str__(self):
        return self.name


class ItemSize(Model):
    item = ForeignKey(Item, on_delete=CASCADE, related_name='itemsize')
    size = ForeignKey(Size, on_delete=CASCADE, related_name='itemsize')
    is_in_stock = BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размер'
        constraints = [
            UniqueConstraint(
                fields=('item', 'size'), name='unique-item-size'
            )
        ]

    def __str__(self):
        return f'{self.item}-{self.size}-{self.is_in_stock}'


class ImageItem(Model):
    image = ImageField(upload_to='items_images')
    item = ForeignKey(
        Item, related_name='imageitem', on_delete=CASCADE
    )
    is_published = BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return f'{self.item}-{self.image}-{self.is_published}'


class Gig(Model):
    city = CharField(max_length=64)
    image = ImageField(upload_to='gigs_images')
    date = CharField(max_length=10)
    time = CharField(max_length=5)
    place = CharField(max_length=128)
    price = IntegerField()
    tickets_url = TextField()

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'

    def __str__(self):
        return f'Концерт в {self.city}'
