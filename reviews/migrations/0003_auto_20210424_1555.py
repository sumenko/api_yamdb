# Generated by Django 3.0.5 on 2021-04-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210424_1549'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='author-title-constraint',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'id'), name='author-title-constraint'),
        ),
    ]
