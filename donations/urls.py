from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'donations'
urlpatterns = [
     path('', TemplateView.as_view(template_name="donations/index.html"), name='homepage'),
     path('logout/', views.logout_view, name='logout'),
     path('donationlist/', views.DonationsListView.as_view(), name="donation_list"),
     path('donationform/', views.donationform, name = "donationform"),
     path('donationlist/saveform', views.saveform, name = "saveform"),
     path('donationlist/<int:pk>/remove', views.DeleteDonationFormView.as_view(), name='delete_donation'),
     path('makedonation/<int:pk>', views.MakeDonationView.as_view(), name="makedonation"),
     path('<int:id>/charge/', views.charge, name='charge'),
     path('success/<str:args>/', views.successMsg, name="success"),
     path('volunteer-post/', views.volunteerform, name='volunteer-post'),
     path('volunteer-list/', views.VolunteerListView.as_view(), name='volunteer-list'),
     path('volunteer-list/edit/<int:pk>', views.UpdateVolunteerFormView.as_view(), name='update_volunteering'),
     path('volunteer-list/<int:pk>/remove', views.DeleteVolunteerFormView.as_view(), name='delete_volunteering'),
]
