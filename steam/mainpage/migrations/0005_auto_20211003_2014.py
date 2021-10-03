# Generated by Django 3.2.6 on 2021-10-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_alter_product_title_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail_images',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='detail_images', verbose_name='Подробная картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='title_images', verbose_name='Главная картинка'),
        ),
    ]