from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm




    # Register view

def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created successfully 🐊")
            return redirect('login')#......................................................
        else:
            messages.error(request, "Error please try again!")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {'form': form})


    #Profile view

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, " 🫎 welcome to the home page  🫎")
            return redirect('profile')

        else:
            messages.error(request, "error please login with correct email or password")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {'form': form})


def ProfileView(request):
    return render(request, 'blog/profile.html')

def LogoutView(request):
    logout(request)
    return redirect('login')