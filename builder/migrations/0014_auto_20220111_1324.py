# Generated by Django 3.0.9 on 2022-01-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0013_auto_20220111_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
