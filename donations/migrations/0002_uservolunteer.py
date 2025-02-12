# Generated by Django 3.1.1 on 2020-11-05 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVolunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=50)),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_time', models.TimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_volunteer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
