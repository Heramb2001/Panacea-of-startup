# Generated by Django 4.1.7 on 2023-03-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_profile_foundereducation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.TextField(blank=True),
        ),
    ]
