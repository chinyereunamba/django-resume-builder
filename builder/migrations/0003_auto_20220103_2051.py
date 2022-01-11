# Generated by Django 3.0.9 on 2022-01-03 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20220101_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersonalinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.UserPersonalInfo'),
        ),
    ]