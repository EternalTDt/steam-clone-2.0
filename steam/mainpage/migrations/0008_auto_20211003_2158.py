# Generated by Django 3.2.6 on 2021-10-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_product_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='disk_storage',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Место на диске'),
        ),
        migrations.AddField(
            model_name='product',
            name='os',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Операционная система'),
        ),
        migrations.AddField(
            model_name='product',
            name='processor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Процессор'),
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Оперативная память'),
        ),
        migrations.AddField(
            model_name='product',
            name='video_card',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Видеокарта'),
        ),
    ]
