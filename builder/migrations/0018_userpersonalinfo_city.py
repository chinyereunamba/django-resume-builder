# Generated by Django 3.0.9 on 2022-01-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0017_remove_skill_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersonalinfo',
            name='city',
            field=models.CharField(default='San Francisco', max_length=20),
        ),
    ]