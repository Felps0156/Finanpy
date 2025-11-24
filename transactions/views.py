from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from transactions.forms import TransactionForm
from transactions.models import Transaction


class TransactionQuerysetMixin(LoginRequiredMixin):
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).select_related('account', 'category')


class TransactionListView(TransactionQuerysetMixin, ListView):
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'


class TransactionCreateView(TransactionQuerysetMixin, CreateView):
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(TransactionQuerysetMixin, UpdateView):
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TransactionDeleteView(TransactionQuerysetMixin, DeleteView):
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:list')
