# Generated by Django 4.1.7 on 2023-03-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_profile_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='establishment',
            field=models.TextField(blank=True),
        ),
    ]