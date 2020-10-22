from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.utils import timezone

from .forms import VolunteerForm

from .models import Donation, VolunteerPost

import stripe

stripe.api_key = "sk_test_51HelJXIC2I2MvSECp2y3PQgivhTUNzwM8CuqoYOpmTgUsqsqHZwitXuaqpkQYliH1C6VM8kvaB2HLdrGHkncousZ00wWWrZ4uk"

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

def makedonation(request):
	return render(request, 'donations/makedonation.html')


def charge(request):
	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			source=request.POST['stripeToken']
			)
		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Donation"
			)
	return redirect(reverse('donations:success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'donations/success.html', {'amount':amount})

class VolunteerFormView(generic.CreateView):
    model = VolunteerPost
    form_class = VolunteerForm
    template_name = 'donations/volunteer_post.html'

    def get_success_url(self):
        return reverse('donations:homepage')

class VolunteerListView(generic.ListView):
    template_name = 'donations/volunteer_list.html'
    context_object_name = 'volunteer_opportunities'

    def get_queryset(self):
        return VolunteerPost.objects.filter(
            date__gte=timezone.now(), 
            # date__lte=timezone.now() + timezone.timedelta(days=100),
        )