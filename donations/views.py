from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

from .models import Donation

def logout_view(request):
    logout(request)
    return redirect("donations:loggedout")

class DonationsView(generic.ListView):
    template_name = 'donations/donation_form.html'
    context_object_name = 'donation_list'
    def get_queryset(self):
        return Donation.objects.filter()

class DonationForm(forms.ModelForm):
    class Meta:
        model= Donation
        fields= ["name", "description", "goal", "end_date"]

def showform(request):
    form = DonationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return HttpResponseRedirect(reverse('donations:donation_list'))

class DonationsListView(generic.ListView):
    template_name = 'donations/donation_list.html'
    context_object_name = 'donation_list'
    def get_queryset(self):
        return Donation.objects.filter()