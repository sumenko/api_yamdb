from api.models import Title
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Review(models.Model):
    title_id = models.ForeignKey(
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
            models.UniqueConstraint(fields=['author', 'title_id'],
                                    name='author-title-constraint')
        ]
