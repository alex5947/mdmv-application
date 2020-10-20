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

