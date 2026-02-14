from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at', 'image_preview')
    search_fields = ('name', 'description')
    list_filter = ('is_available', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "Немає зображення"
    image_preview.short_description = 'Прев`ю'