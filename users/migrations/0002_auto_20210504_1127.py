# Generated by Django 3.0.5 on 2021-05-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='', max_length=100, verbose_name='Код подтверждения'),
        ),
    ]