from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from api.validators import year_validator


class Roles(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class Category(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Короткая ссылка', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('slug',)


class Genre(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Короткая ссылка', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('slug',)


class Title(models.Model):
    name = models.CharField('Название', max_length=200)
    year = models.SmallIntegerField(
        'Год создания',
        validators=[year_validator],
    )
    rating = models.SmallIntegerField(
        'Рейтинг',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        blank=True,
        null=True,
    )
    description = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        db_index=False,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles',
        blank=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('id',)
