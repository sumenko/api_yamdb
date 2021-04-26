from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models import Title

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Объект',
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=False,
        null=True,
        db_index=False,
    )
    author = models.ForeignKey(User,
                               verbose_name='Автор отзыва',
                               on_delete=models.CASCADE,
                               related_name='authors',
                               )
    text = models.TextField(verbose_name='Текст отзыва', blank=False)
    score = models.IntegerField(verbose_name='Оценка',
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='author-title-constraint')
        ]


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments',
        blank=False,
        null=True,
        db_index=False,
    )
    text = models.TextField(verbose_name='Текст комментария', blank=False)
    author = models.ForeignKey(User,
                               verbose_name='Автор комментария',
                               on_delete=models.CASCADE,
                               related_name='comments',
                               )
    pub_date = models.DateTimeField('Дата комментария', auto_now_add=True)
