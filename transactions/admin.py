from django.contrib import admin

from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'date', 'account', 'user')
    list_filter = ('category__type', 'date')
    search_fields = ('description', 'category__name', 'account__name', 'user__email')
