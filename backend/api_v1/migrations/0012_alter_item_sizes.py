# Generated by Django 4.2.17 on 2025-01-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0011_remove_shoppingcart_unique_user_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sizes',
            field=models.ManyToManyField(blank=True, null=True, related_name='itemsizes', through='api_v1.ItemSize', to='api_v1.size'),
        ),
    ]
