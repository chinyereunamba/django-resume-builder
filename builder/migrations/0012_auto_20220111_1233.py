# Generated by Django 3.0.9 on 2022-01-11 11:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0011_auto_20220110_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='userSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ManyToManyField(to='builder.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.UserPersonalInfo')),
            ],
        ),
    ]