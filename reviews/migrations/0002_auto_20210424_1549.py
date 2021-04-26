# Generated by Django 3.0.5 on 2021-04-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title_id'), name='author-title-constraint'),
        ),
    ]
