# Generated by Django 3.0.9 on 2022-01-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20220103_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='userpersonalinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_img.png', null=True, upload_to=''),
        ),
    ]
