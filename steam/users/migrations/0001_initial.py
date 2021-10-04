# Generated by Django 3.2.6 on 2021-10-04 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='default.jpg', upload_to='user_images', verbose_name='Фото')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('country', django_countries.fields.CountryField(default='', max_length=2, verbose_name='Страна')),
                ('address', models.CharField(default='', max_length=250, verbose_name='Адрес')),
                ('city', models.CharField(default='', max_length=100, verbose_name='Населенный пункт')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
