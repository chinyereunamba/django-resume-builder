# Generated by Django 3.0.9 on 2022-01-01 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='builder.UserPersonalInfo'),
        ),
    ]