from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# source:
# https://testdriven.io/blog/django-custom-user-model/

class CustomUser(AbstractUser):
    # username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
