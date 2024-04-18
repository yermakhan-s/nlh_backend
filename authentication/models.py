from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import URLValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    class ROLES:
        USER = 'user'
        EVENT_MANAGER = 'event_manager'
        ROLES_CHOICES = (
            (USER, "Юзер"), (EVENT_MANAGER , "Ивент менеджер"))

    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    telegram_url = models.URLField(max_length=200, blank=True, null=True)
    avatar_url = models.FileField(null=True, blank=True)
    first_name = None
    last_name = None
    role = models.CharField(max_length=1000, choices=ROLES.ROLES_CHOICES, default='user', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username



