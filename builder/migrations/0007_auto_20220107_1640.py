# Generated by Django 3.0.9 on 2022-01-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_auto_20220107_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='label',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='social',
            name='link',
            field=models.URLField(max_length=255),
        ),
    ]