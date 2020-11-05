import datetime
from django.contrib.auth.models import User

from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=50, default = "")
    description = models.CharField(max_length=500, default = "")
    goal = models.IntegerField(default = 0)
    total = models.IntegerField(default = 0)
    end_date = models.DateField(default = datetime.date.today)
    creator = models.CharField(max_length=50, default = "")

    def date_in_future(self):
        now = timezone.now()
        return now <= self.date

class UserDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_donation", null=True)
    name = models.CharField(max_length=50, default = "")
    amount = models.IntegerField(default = 0)

class VolunteerPost(models.Model):
    title = models.TextField(default = "", max_length=50)
    name = models.TextField(default = "", max_length=50)
    date = models.DateField(default = datetime.date.today)
    start_time = models.TimeField(default = timezone.now)
    end_time = models.TimeField(default = timezone.now)
    description = models.TextField(default = "") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def date_in_future(self):
        now = timezone.now()
        return now <= self.date

    def end_time_after_start_time(self):
        return self.start_time < self.end_time