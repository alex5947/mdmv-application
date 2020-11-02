from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'donations'
urlpatterns = [
     path('', TemplateView.as_view(template_name="donations/index.html"), name='homepage'),
     path('logout/', views.logout_view, name='logout'),
     path('donationform/', views.DonationsView.as_view(), name='donation_form'),
     path('donationlist/', views.DonationsListView.as_view(), name="donation_list"),
     path('donationlist/showform', views.showform, name = "showform"),
     path('donationlist/saveform', views.saveform, name = "saveform"),
     path('makedonation/', views.makedonation, name="makedonation"),
     path('charge/', views.charge, name='charge'),
     path('success/<str:args>/', views.successMsg, name="success"),
     path('volunteer-post/', views.VolunteerFormView.as_view(), name='volunteer-post'),
     path('volunteer-list/', views.VolunteerListView.as_view(), name='volunteer-list'),
]
