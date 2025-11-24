from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from categories.forms import CategoryForm
from categories.models import Category


class CategoryQuerysetMixin(LoginRequiredMixin):
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryListView(CategoryQuerysetMixin, ListView):
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CategoryQuerysetMixin, CreateView):
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('categories:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(CategoryQuerysetMixin, UpdateView):
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('categories:list')


class CategoryDeleteView(CategoryQuerysetMixin, DeleteView):
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('categories:list')
