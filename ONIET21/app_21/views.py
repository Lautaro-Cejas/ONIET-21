from django.shortcuts import redirect, render
from datetime import date, datetime
from .forms import UserLoginForm
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required

# Create your views here.
def Inicio(request):
    fecha = datetime.now()

    return render(request, 'index.html', {'fecha':fecha})

def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['usuario']
            messages.success(request, f'Usuario {usuario} creado')
            return redirect('barrios.html')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form':form})

@login_required
def barrios(request):
    a = requests
    b = BeautifulSoup
    pass

def Logout(request):
    pass

def Account(request):
    pass
