from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


class ProductType(models.Model):
    name = models.CharField("Тип товара", max_length=255)
    
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self) -> str:
        return self.name


class CommonRequirements(models.Model):
    processor = models.CharField("Процессор", max_length=100, blank=True, null=True)
    video_card = models.CharField("Видеокарта", max_length=100, blank=True, null=True)
    os = models.CharField("Операционная система", max_length=100, blank=True, null=True)
    ram = models.CharField("Оперативная память", max_length=100, blank=True, null=True)
    disk_storage = models.CharField("Место на диске", max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("Ссылка", max_length=130, unique=True, blank=True, null=True)
    year_of_foundation = models.PositiveSmallIntegerField("Год основания", default=2010)
    foundation_country = CountryField()
    ceo = models.CharField("Генеральный директор", max_length=40)
    employees_num = models.IntegerField("Количество сотрудников", default=0)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"



class Product(CommonRequirements):
    name = models.CharField("Название", max_length=150, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, related_name="type", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField("Ссылка", max_length=130, unique=True, blank=True, null=True)
    description = RichTextField()
    release_date = models.DateField("Дата выхода", auto_now_add=True)
    price = models.DecimalField("Стоимость", max_digits=10, decimal_places=2, blank=True)
    title_image = models.ImageField("Главная картинка", default="default.jpg", upload_to="title_images", blank=True)
    company = models.ManyToManyField(Company, related_name="company", verbose_name="Компания")
    detail_images = models.ImageField("Подробная картинка", default="default.jpg", upload_to="detail_images", blank=True)
    platforms = models.CharField("Платформы", max_length=150, blank=True)
    store_image = models.ImageField("Картинка в каталоге", default="default.jpg", upload_to="store_images", blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"