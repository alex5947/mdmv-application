from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

from .models import Donation

def logout_view(request):
    logout(request)
    return redirect("donations:loggedout")