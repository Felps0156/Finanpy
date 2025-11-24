from django.urls import path

from accounts.views import (
    AccountCreateView,
    AccountDeleteView,
    AccountListView,
    AccountUpdateView,
)


app_name = 'accounts'

urlpatterns = [
    path('contas/', AccountListView.as_view(), name='list'),
    path('contas/nova/', AccountCreateView.as_view(), name='create'),
    path('contas/<int:pk>/editar/', AccountUpdateView.as_view(), name='update'),
    path('contas/<int:pk>/excluir/', AccountDeleteView.as_view(), name='delete'),
]
