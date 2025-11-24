from django.conf import settings
from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.PROTECT,
        related_name='transactions',
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date', '-created_at')

    def __str__(self):
        return f'{self.category.name} - R$ {self.amount}'
