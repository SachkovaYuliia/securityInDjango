from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(lambda request: render(request, 'users/home.html')), name='home'),
    path('users/', include('users.urls')),
]
