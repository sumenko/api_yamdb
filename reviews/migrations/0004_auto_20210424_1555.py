# Generated by Django 3.0.5 on 2021-04-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20210424_1555'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='author-title-constraint',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title_id'), name='author-title-constraint'),
        ),
    ]