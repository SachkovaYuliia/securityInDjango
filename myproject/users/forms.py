from django import forms
from django.contrib.auth.hashers import make_password
from .models import User
from django.utils.html import strip_tags

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password': 'Password',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        """
        Очищаємо введені дані від HTML
        """
        cleaned_data['username'] = strip_tags(cleaned_data.get('username', ''))
        cleaned_data['email'] = strip_tags(cleaned_data.get('email', ''))

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        """
        Хешуємо пароль
        """
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
