from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'donations'
urlpatterns = [
     path('', TemplateView.as_view(template_name="donations/index.html")),
     path('logout/', views.logout_view, name='logout'),
     path('loggedout/', TemplateView.as_view(template_name="donations/loggedout.html"), name='loggedout'),
     path('donationform/', views.DonationsView.as_view(), name='donation_form'),
     path('donationlist/', views.DonationsListView.as_view(), name="donation_list"),
     path('donationlist/showform', views.showform, name = "showform")
]
