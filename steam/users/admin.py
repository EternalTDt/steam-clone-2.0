from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone', 'img')
	list_display_links = ('user', 'phone', 'img')