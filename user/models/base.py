from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError

from django.contrib.auth.base_user import BaseUserManager

from helper.models import CreationModificationBase


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not extra_fields.get('is_superuser'):
            if not email:
                raise ValueError('Email for user must be set.')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        else:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser,CreationModificationBase):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(blank=True)
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="_user_permissions"
    )
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = UserManager()

    def clean(self):
        instances = User.objects.filter(email=self.email)
        if self.id:
            instances = instances.exclude(id=self.id)
        if instances.exists():
            raise ValidationError(
                {'email': 'User with this email already exists.'})

    def __str__(self):
        return str(self.name)