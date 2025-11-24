from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from users.forms import EmailAuthenticationForm, SignupForm


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EmailLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = EmailAuthenticationForm
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True

    def get_success_url(self):
        return self.success_url


class LogoutRedirectView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
