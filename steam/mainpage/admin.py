from django.contrib import admin
from .models import Company, Product, Category, ProductType

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ['name']


admin.site.register(ProductType)