from backend.settings import DATAFILES_DIR

import json


DATAFILES = (
    ('Category', 'categories_test_data.json'),
    ('Size', 'sizes_test_data.json'),
    ('Item', 'items_test_data.json'),
    ('Gig', 'gigs_test_data.json'),
)


def open_json(datafile):
    path = DATAFILES_DIR / datafile
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as ex:
        print(ex)
        return


def load_json():
    for model, datafile in DATAFILES:
        data = open_json(datafile)
        if model == 'Category':
            for category in data:
                Category.objects.get_or_create(
                    name=category['name'], slug=category['slug']
                )
        elif model == 'Size':
            for size in data:
                Size.objects.get_or_create(name=size['name'])
        elif model == 'Item':
            for item in data:
                category_instance = Category.objects.get(id=item['category'])
                Item.objects.get_or_create(
                    name=item['name'], description=item['description'],
                    is_published=item['is_published'],
                    main_image=item['main_image'], category=category_instance,
                    price=item['price']
                )
                item_instance = Item.objects.get(
                    name=item['name'], description=item['description'],
                    is_published=item['is_published'],
                    main_image=item['main_image'], category=category_instance,
                    price=item['price']
                )
                for size in item['sizes']:
                    size_instance = Size.objects.get(id=size)
                    ItemSize.objects.get_or_create(
                        item=item_instance, size=size_instance,
                        is_in_stock=True
                    )
                for image in item['images']:
                    ImageItem.objects.get_or_create(
                        image=image, item=item_instance, is_published=True
                    )
        elif model == 'Gig':
            for gig in data:
                Gig.objects.get_or_create(
                    city=gig['city'], image=gig['image'], date=gig['date'],
                    time=gig['time'], place=gig['place'], price=gig['price'],
                    tickets_url=gig['tickets_url'],
                    is_published=gig['is_published']
                )

        print(f'{datafile} objects created')


if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    django.setup()
    from api_v1.models import (
        Category, Size, Item, ItemSize, ImageItem, Gig
    )
    load_json()

