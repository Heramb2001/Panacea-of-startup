# Generated by Django 4.2 on 2023-05-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_jobpost_jobcompany_jobpost_jobexperience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='jobcompany',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='jobexperience',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='jobmode',
            field=models.TextField(),
        ),
    ]
