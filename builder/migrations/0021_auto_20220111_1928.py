# Generated by Django 3.0.9 on 2022-01-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0020_auto_20220111_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='study_field',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
