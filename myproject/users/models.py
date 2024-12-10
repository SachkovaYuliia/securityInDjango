from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .utils import execute_secure_query

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError(" Please enter email address")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @classmethod
    def get_users_by_email(cls, email):
        query = "SELECT * FROM users_user WHERE email = %s"
        params = [email]
        return execute_secure_query(query, params)

    def __str__(self):
        return self.username
