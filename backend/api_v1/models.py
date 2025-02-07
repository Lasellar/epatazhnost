from django.db.models import (
    Model, CharField, IntegerField, ForeignKey, BooleanField,
    ManyToManyField, SlugField, TextField, CASCADE, ImageField, UniqueConstraint, DateTimeField
)
from django.urls import reverse


class Category(Model):
    """Модель категории."""
    name = CharField(max_length=30, unique=True)
    slug = SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Size(Model):
    """Модель размера для вещи."""
    name = CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Item(Model):
    """Модель вещи."""
    name = CharField(max_length=64)
    description = TextField()
    sizes = ManyToManyField(
        Size, related_name='itemsizes', through='ItemSize'
    )
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
    """Модель для связи вещей и размеров."""
    item = ForeignKey(Item, on_delete=CASCADE, related_name='itemsize')
    size = ForeignKey(
        Size, on_delete=CASCADE, related_name='itemsize',
        blank=True, null=True
    )
    amount = IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размер'
        constraints = [
            UniqueConstraint(
                fields=('item', 'size'), name='unique-item-size'
            )
        ]

    def __str__(self):
        return f'{self.item}-{self.size}-{self.amount}'


class ImageItem(Model):
    """Модель для связи вещей и картинок."""
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
    """Модель концерта."""
    city = CharField(max_length=64)
    image = ImageField(upload_to='gigs_images')
    date = CharField(max_length=10)
    time = CharField(max_length=5)
    place = CharField(max_length=128)
    price = IntegerField()
    tickets_url = TextField()
    is_published = BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'

    def __str__(self):
        return f'Концерт в {self.city}'


class ShoppingCart(Model):
    """Модель корзины покупок."""
    user_cookie = CharField(max_length=60)
    item = ForeignKey(
        Item, on_delete=CASCADE, related_name='shoppingcart'
    )
    created = DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ('user_cookie',)
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.item.name} в списке покупок у {self.user_cookie}'


class UserInfo(Model):
    cookie = CharField(max_length=60)
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    third_name = CharField(max_length=64)
    telegram = CharField(max_length=1024)
    sdek = CharField(max_length=1024)

    class Meta:
        verbose_name = 'Инфо о пользователе'
        verbose_name_plural = 'Инфо о пользователях'

    def __str__(self):
        return (
            f'[{self.cookie}] - {self.first_name} {self.last_name} '
            f'{self.third_name} tg: {self.telegram} SDEK: {self.sdek}'
        )


class Order(Model):
    user = ForeignKey(UserInfo, on_delete=CASCADE)
    items = ManyToManyField(
        Item, related_name='orderitems', through='ItemOrder'
    )
    created = DateTimeField(auto_now=True, blank=True)


class ItemOrder(Model):
    item = ForeignKey(Item, on_delete=CASCADE, related_name='itemorder')
    order = ForeignKey(
        Order, on_delete=CASCADE, related_name='itemorder',
        blank=True, null=True
    )


class PromoCode(Model):
    name = CharField(max_length=100)
    code = CharField(max_length=16, unique=True)
    discount = IntegerField(verbose_name='скидка в %')
    amount = IntegerField()

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

    def __str__(self):
        return f'[{self.code}] {self.name}, остаток: {self.amount}'


class MainPagePhoto(Model):
    image = ImageField(upload_to='main_page_images')
    is_published = BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = 'Фото с главной страницы'
        verbose_name_plural = 'фото с главной страницы'


class Bot(Model):
    chat_id = CharField(max_length=14)
    message = TextField()

    class Meta:
        verbose_name = 'Бот'

    def get_ansolute_url(self):
        return reverse(
            'api_v1:send_message_by_bot',
            kwargs={'chat_id': self.chat_id, 'message': self.message}
        )
