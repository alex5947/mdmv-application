from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('donations.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]