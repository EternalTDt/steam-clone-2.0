from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    img = models.ImageField("Фото", default='default.jpg', upload_to='user_images')
    phone = models.CharField("Телефон", max_length=50, blank=True)
    country = CountryField('Страна', default='')
    address = models.CharField('Адрес', max_length=250, default='')
    city = models.CharField('Населенный пункт', max_length=100, default='')
    
    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
        
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"