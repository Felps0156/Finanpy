from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import TemplateView

from accounts.models import Account
from categories.models import Category
from transactions.models import Transaction


def home(request):
    return render(request, 'core/home.html')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        transactions = Transaction.objects.filter(user=user).select_related('category', 'account')

        entries = transactions.filter(category__type=Category.TYPE_INCOME).aggregate(total=Sum('amount'))['total'] or Decimal('0')
        exits = transactions.filter(category__type=Category.TYPE_EXPENSE).aggregate(total=Sum('amount'))['total'] or Decimal('0')
        accounts_total = Account.objects.filter(user=user).aggregate(total=Sum('balance'))['total'] or Decimal('0')

        context.update(
            {
                'total_entries': entries,
                'total_exits': exits,
                'accounts_total': accounts_total,
                'recent_transactions': transactions.order_by('-date', '-created_at')[:5],
            }
        )
        return context
