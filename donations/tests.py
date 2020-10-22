from django.test import TestCase, RequestFactory

from .models import VolunteerPost
from .views import VolunteerFormView, VolunteerListView

import datetime
from django.utils import timezone

# Create your tests here.
class VolunteerPostTestCase(TestCase):
    def test_opportunity_date_in_past(self):
        """
        date_in_future() returns False for volunteer posts with dates in the past
        """
        day = timezone.now() - datetime.timedelta(days=5)
        past_post = VolunteerPost(date=day)
        self.assertIs(past_post.date_in_future(), False)

    def test_opportunity_date_in_present(self):
        """
        date_in_future() returns True for volunteer posts with dates in the present
        """
        day = timezone.now() 
        past_post = VolunteerPost(date=day)
        self.assertIs(past_post.date_in_future(), True)

    def test_opportunity_date_in_future(self):
        """
        date_in_future() returns False for volunteer posts with dates in the future
        """
        day = timezone.now() + datetime.timedelta(days=123)
        past_post = VolunteerPost(date=day)
        self.assertIs(past_post.date_in_future(), True)

    def test_opportunity_start_time_before_end_time(self):
        """
        end_time_after_start_time() returns True for volunteer posts with start_time before end_time
        """
        end = timezone.now()
        start = end - timezone.timedelta(hours=2)
        post = VolunteerPost(start_time=start, end_time=end)
        self.assertIs(post.end_time_after_start_time(), True)

    def test_opportunity_start_time_equal_end_time(self):
        """
        end_time_after_start_time() returns False for volunteer posts with start_time at the time as end_time
        """
        end = timezone.now()
        start = timezone.now()
        post = VolunteerPost(start_time=start, end_time=end)
        self.assertIs(post.end_time_after_start_time(), False)

    def test_opportunity_start_time_after_end_time(self):
        """
        end_time_after_start_time() returns False for volunteer posts with start_time after end_time
        """
        end = timezone.now()
        start = end + timezone.timedelta(hours=2)
        post = VolunteerPost(start_time=start, end_time=end)
        self.assertIs(post.end_time_after_start_time(), False)
    