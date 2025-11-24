from django.urls import path

from categories.views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
)


app_name = 'categories'

urlpatterns = [
    path('categorias/', CategoryListView.as_view(), name='list'),
    path('categorias/nova/', CategoryCreateView.as_view(), name='create'),
    path('categorias/<int:pk>/editar/', CategoryUpdateView.as_view(), name='update'),
    path('categorias/<int:pk>/excluir/', CategoryDeleteView.as_view(), name='delete'),
]
