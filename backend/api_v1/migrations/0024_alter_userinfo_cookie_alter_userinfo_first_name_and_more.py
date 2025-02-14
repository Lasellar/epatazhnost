# Generated by Django 4.2.17 on 2025-02-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0023_alter_userinfo_telegram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='cookie',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sdek',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='third_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
