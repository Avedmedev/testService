from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

#from women.models import Women, Category
from myTest.forms import RegisterUserForm, LoginUserForm

from myTest.utils import DataMixin


def index(request):
    context = {'title': 'Main page'}
    return render(request, 'myTest\index.html', context=context)    


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'myTest/register.html'
    success_url = reverse_lazy('log_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'myTest/login.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('log_in')


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена.</h1>")