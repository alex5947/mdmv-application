# Generated by Django 3.1.1 on 2020-11-05 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0011_userdonation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdonation',
            old_name='goal',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='userdonation',
            name='total',
        ),
        migrations.AlterField(
            model_name='userdonation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_donation', to=settings.AUTH_USER_MODEL),
        ),
    ]
