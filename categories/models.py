from django.conf import settings
from django.db import models


class Category(models.Model):
    TYPE_INCOME = 'entrada'
    TYPE_EXPENSE = 'saida'
    TYPE_CHOICES = [
        (TYPE_INCOME, 'Entrada'),
        (TYPE_EXPENSE, 'Saída'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.type})'
