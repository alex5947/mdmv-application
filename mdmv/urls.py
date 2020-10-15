from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    #path('donations/', include('donations.urls')),
    #path('', include('donations.urls')),
    path('', TemplateView.as_view(template_name="donations/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]