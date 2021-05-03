from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user', 'Пользователь'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN = 'admin', 'Администратор'

    email = models.EmailField(verbose_name='email',
                              unique=True, blank=False)
    bio = models.TextField(verbose_name='О себе', blank=True)
    role = models.CharField(verbose_name='Тип пользователя', max_length=20,
                            choices=Roles.choices, default=Roles.USER)
    confirmation_code = models.CharField(verbose_name='Код подтверждения',
                                         null=True, default='', max_length=100)

    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.Roles.MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)


# class ConfirmationCode(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     confirmation_code = models.CharField(verbose_name='Код подтверждения',
#                                          null=True, default='', max_length=100)
