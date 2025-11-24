from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.forms import AccountForm
from accounts.models import Account


class AccountQuerysetMixin(LoginRequiredMixin):
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class AccountListView(AccountQuerysetMixin, ListView):
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'


class AccountCreateView(AccountQuerysetMixin, CreateView):
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = reverse_lazy('accounts:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(AccountQuerysetMixin, UpdateView):
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = reverse_lazy('accounts:list')


class AccountDeleteView(AccountQuerysetMixin, DeleteView):
    template_name = 'accounts/account_confirm_delete.html'
    success_url = reverse_lazy('accounts:list')
