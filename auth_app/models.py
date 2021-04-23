from django.contrib.auth.models import AbstractUser
from django.db import models


# FIXME сделать одно для всех
class Roles(models.TextChoices):
    '''model for roles'''
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'

ROLES = [
    ('admin', 'admin'),
    ('user', 'user'),
    ('moderator', 'moderator'),
]

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLES,
                            default='user')
    confirmation_code = models.CharField(null=True, default='', max_length=100)
    class Meta:
        ordering = ["-id"]
