from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import *
from .models import *
from .utils import DataMixin


def index(request):
    return render(request,'main/index.html')


def damn(request):
    return render(request,'main/damn.html')


def create(request):
    Heroes = Heroe.objects.all()
    Users = User.objects.all()
    if request.method == "POST":
        form = Sborki()
        form.heroe = Heroe.objects.get(name=request.POST.get("heroe"))
        form.user = User.objects.get(username=request.POST.get("user"))
        form.text = request.POST.get("text")
        form.save()
    return HttpResponseRedirect("/", {"Heroes": Heroes, "Users": Users})


def Abaddon(request):
    Users = User.objects.all()
    Heroes = Heroe.objects.filter(name="Abaddon")
    Conters = Conter.objects.filter(heroe=1)
    Sborkis = Sborki.objects.filter(heroe=1)
    return render(request, "main/Abaddon.html", {"Heroes": Heroes, "Conters": Conters, "Sborkis": Sborkis, "Users": Users})


def Axe(request):
    Users = User.objects.all()
    Heroes = Heroe.objects.filter(name="Axe")
    Conters = Conter.objects.filter(heroe=5)
    Sborkis = Sborki.objects.filter(heroe=5)
    return render(request, "main/Abaddon.html", {"Heroes": Heroes, "Conters": Conters, "Sborkis": Sborkis, "Users": Users})


def Pudge(request):
    Users = User.objects.all()
    Heroes = Heroe.objects.filter(name="Pudge")
    Conters = Conter.objects.filter(heroe=4)
    Sborkis = Sborki.objects.filter(heroe=4)
    return render(request, "main/Abaddon.html", {"Heroes": Heroes, "Conters": Conters, "Sborkis": Sborkis, "Users": Users})


def Morphling(request):
    Users = User.objects.all()
    Heroes = Heroe.objects.filter(name="Morphling")
    Conters = Conter.objects.filter(heroe=3)
    Sborkis = Sborki.objects.filter(heroe=3)
    return render(request, "main/Abaddon.html", {"Heroes": Heroes, "Conters": Conters, "Sborkis": Sborkis, "Users": Users})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('log')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/log.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('log')