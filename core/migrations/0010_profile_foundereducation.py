# Generated by Django 4.1.7 on 2023-03-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_profile_founderage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='foundereducation',
            field=models.TextField(blank=True),
        ),
    ]
