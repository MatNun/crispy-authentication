# Generated by Django 4.0.6 on 2022-07-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='Minimum 8 characters', max_length=40),
        ),
    ]
