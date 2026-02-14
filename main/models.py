from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Зображення')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    is_available = models.BooleanField(default=True, verbose_name='Доступний')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'