from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'donations'
urlpatterns = [
     path('', TemplateView.as_view(template_name="donations/index.html")),
     path('logout/', views.logout_view, name='logout'),
     path('loggedout/', TemplateView.as_view(template_name="donations/loggedout.html"), name='loggedout'),
]
