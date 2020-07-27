from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib import messages
from .models import FormItems
from strona.models import Pageitem as P
from meetap.settings import LANGUAGES as L
from meetap.core.classes import PageLoad
from django.contrib.auth.forms import AuthenticationForm
from .forms import ExtendedCreationForm


# Formularz rejestracji.
def register(request):
    if request.method == 'POST':
        form = ExtendedCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            # Sprawdza shaszowane dane powyżej w bazie danych.
            login(request, user)
            return redirect('home')
            # Przekierowuje na stronę główną zalogowanego usera.
    else:
        form = ExtendedCreationForm()
    locations = list(FormItems.objects.all())
    items = locations[0]
    context = {'form': form,
               'item': items, }
    template = 'registration/register.html'
    return render(request, template, context)


# Formularz logowania.
def logger(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()
    locations = list(FormItems.objects.all())
    items = locations[0]
    locations1 = list(P.objects.all())
    items1 = locations1[0]
    template = 'registration/login.html'
    context = {'form': form,
               'item': items,
               'item1': items1, }
    return render(request, template, context)

# def unlogger(request):
