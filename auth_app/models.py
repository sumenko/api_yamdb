from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user', 'Пользователь'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN = 'admin', 'Администратор'

    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=Roles.choices,
                            default=Roles.USER)
    confirmation_code = models.CharField(null=True, default='', max_length=100)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
