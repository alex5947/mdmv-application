# Generated by Django 3.1.1 on 2020-11-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_uservolunteer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerpost',
            name='end_time',
            field=models.TimeField(default='00:00-23:59'),
        ),
        migrations.AlterField(
            model_name='volunteerpost',
            name='start_time',
            field=models.TimeField(default='00:00-23:59'),
        ),
    ]
