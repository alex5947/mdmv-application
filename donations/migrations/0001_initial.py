# Generated by Django 3.1.1 on 2020-10-23 03:09

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=500)),
                ('goal', models.IntegerField(default=0)),
                ('end_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=50)),
                ('name', models.TextField(default='', max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_time', models.TimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
