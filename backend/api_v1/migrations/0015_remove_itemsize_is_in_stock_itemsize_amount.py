# Generated by Django 4.2.17 on 2025-01-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0014_alter_item_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsize',
            name='is_in_stock',
        ),
        migrations.AddField(
            model_name='itemsize',
            name='amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
