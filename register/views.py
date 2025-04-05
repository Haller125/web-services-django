from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, AdminRegistrationForm
from django.contrib.auth.decorators import login_required
import requests
from .decorators import admin_required
from .models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user_currency = form.cleaned_data.get('currency')
            default_money = requests.get(f'http://localhost:8000/webapps2025/conversion/usd/{user_currency}/750')
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'register/home.html', {'user': request.user})

# TODO: add template
@admin_required
def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user_currency = form.cleaned_data.get('currency')
            default_money = requests.get(f'http://localhost:8000/webapps2025/conversion/usd/{user_currency}/750')
            form.save()
            return redirect('home')
    else:
        form = AdminRegistrationForm()
    return render(request, 'register/register.html', {'form': form})


@admin_required
def list_of_users(request):
    users = User.objects.all()
    return render(request, 'register/list_of_users.html', {'users': users})
