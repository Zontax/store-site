from django.contrib import admin

from main.models import BaseAdvertisement


@admin.register(BaseAdvertisement)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'description', 'disable_timestamp']
    list_editable = ['description', 'disable_timestamp', 'is_active']

    fields = [
        'name',
        'description',
        'css_style',
        'image',
        'disable_timestamp',
        'is_active',
    ]
