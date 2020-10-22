import datetime

from django.db import models
from django.db import models
from django.utils import timezone


# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=50, default = "")
    description = models.CharField(max_length=500, default = "")
    goal = models.IntegerField(default = 0)
    end_date = models.DateField(default = datetime.date.today)

class VolunteerPost(models.Model):
    title = models.CharField(max_length=80)
    name = models.CharField(max_length=30)
    date = models.DateField(default = datetime.date.today)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField() 
