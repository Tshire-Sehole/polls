# importing liabraries
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    The function `authenticate_user` authenticates a user based on the provided username and password in
    a Django web application.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:index')
    )
        
@login_required
def login_view(request):
    """
    The `login_view` function handles user authentication and login based on POST request data in a
    Django web application.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')  
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    """
    The `register_view` function handles user registration by validating input, checking for existing
    usernames, creating a new user, and displaying success or error messages.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('user_auth:register_view')  
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('user_auth:register_view') 
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('user_auth:login')  
    return render(request, 'authentication/registration.html')

# logging out funcition
def logout_view(request):
    logout(request)
    return redirect('user_auth:login')