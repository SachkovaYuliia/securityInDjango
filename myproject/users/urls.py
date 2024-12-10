from django.urls import path
from .views import register_view, login_view, logout_view, test_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('test/', test_view, name='test_view'),
]