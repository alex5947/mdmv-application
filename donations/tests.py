from django.test import TestCase, RequestFactory
from django.urls import reverse

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

    #Exclude test to test Travis Build
    # def test_opportunity_date_in_present(self):
    #     """
    #     date_in_future() returns True for volunteer posts with dates in the present
    #     """
    #     day = timezone.now() 
    #     past_post = VolunteerPost(date=day)
    #     self.assertIs(past_post.date_in_future(), True)

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
    
class VolunteerListViewTests(TestCase):
    def create_volunteer_post(date):
        """
        Create a volunteer post with a given date
        """
        return VolunteerPost.objects.create(
            name=""
        )

    def test_no_volunteer_posts(self):
        """
        The volunteer list view displays a message when there are no posts
        """    
        response = self.client.get(reverse('donations:volunteer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Volunteering Opportunities have been posted yet")
        self.assertQuerysetEqual(response.context['volunteer_opportunities'], [])

    def test_past_volunteer_post(self):
        """
        The volunteer list view doesn't display a volunteer post with a date in the past
        """
        past_post = VolunteerPost.objects.create(date=timezone.now() - datetime.timedelta(days=2))
        response = self.client.get(reverse('donations:volunteer-list'))
        self.assertContains(response, "No Volunteering Opportunities have been posted yet")
        self.assertQuerysetEqual(response.context['volunteer_opportunities'], [])

    def test_present_volunteer_post(self):
        """
        The volunteer list view displays a volunteer post with a date in the present
        """
        past_post = VolunteerPost.objects.create(date=timezone.now())
        response = self.client.get(reverse('donations:volunteer-list'))
        self.assertQuerysetEqual(response.context['volunteer_opportunities'], ['<VolunteerPost: VolunteerPost object (1)>'])

    def test_future_volunteer_post(self):
        """
        The volunteer list view displays a volunteer post with a date in the future
        """
        past_post = VolunteerPost.objects.create(date=timezone.now() + datetime.timedelta(days=2))
        response = self.client.get(reverse('donations:volunteer-list'))
        self.assertQuerysetEqual(response.context['volunteer_opportunities'], ['<VolunteerPost: VolunteerPost object (1)>'])
    

