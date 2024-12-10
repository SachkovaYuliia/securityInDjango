from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .utils import execute_secure_query

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'users/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def test_view(request):
    username = "Ivan"
    query = "SELECT * FROM users_user WHERE username = %s"
    params = [username]

    results = execute_secure_query(query, params)

    return render(request, 'users/results.html', {'results': results})