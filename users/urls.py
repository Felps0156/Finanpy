from django.urls import path

from users.views import EmailLoginView, LogoutRedirectView, SignupView


app_name = 'users'

urlpatterns = [
    path('login/', EmailLoginView.as_view(), name='login'),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),
    path('cadastro/', SignupView.as_view(), name='signup'),
]
