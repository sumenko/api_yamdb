from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [
        ('admin', 'admin'),
        ('user', 'user'),
        ('moderator', 'moderator'),
    ]
    email = models.EmailField(unique=True, blank=False)
    description = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLES,
                            default='user')
    confirmation_code = models.CharField(null=True, default='', max_length=100)
