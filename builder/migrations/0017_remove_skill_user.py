# Generated by Django 3.0.9 on 2022-01-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0016_skill_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
    ]
