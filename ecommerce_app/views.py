from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from models import User

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        # Handle login logic here
        return redirect('home')
    return render(request, 'login.html')

def seller_dashboard(request):
    return render(request, 'seller_dashboard.html')

def buyer_dashboard(request):
    return render(request, 'buyer_dashboard.html')
