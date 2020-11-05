from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.utils import timezone

from .forms import VolunteerForm

from .models import Donation, VolunteerPost, UserDonation, UserVolunteer

import stripe

stripe.api_key = "sk_test_51HelJXIC2I2MvSECp2y3PQgivhTUNzwM8CuqoYOpmTgUsqsqHZwitXuaqpkQYliH1C6VM8kvaB2HLdrGHkncousZ00wWWrZ4uk"

def logout_view(request):
    logout(request)
    return redirect("donations:homepage")

class DonationsView(generic.ListView):
    template_name = 'donations/donation_form.html'
    context_object_name = 'donation_list'
    def get_queryset(self):
        return Donation.objects.filter()

class MakeDonationView(generic.ListView):
    template_name = 'donations/makedonation.html'
    context_object_name = 'donation'
    def get_queryset(self, *args, **kwargs):
        return Donation.objects.filter(id=self.kwargs['pk'])

class DonationForm(forms.ModelForm):
    class Meta:
        model= Donation
        fields= ["name", "description", "goal", "end_date"]
        exclude = ["creator"]

class UserDonationForm(forms.ModelForm):
    class Meta:
        model= UserDonation
        fields = ["name", "amount"]

def donationform(request):
    form = DonationForm(request.POST or None)
    if form.is_valid():
        donation = form.save(commit = False)
        donation.creator = request.user
        donation.save()
        return HttpResponseRedirect(reverse('donations:donation_list'))
    context = {'form': form}
    return render(request, 'donations/donation_form.html', context)

def saveform(response):
    return HttpResponseRedirect(reverse('donations:homepage'))

class DeleteDonationFormView(generic.DeleteView):
    model = Donation
    template_name = 'donations/delete_donation.html'

    def get_success_url(self):
        return reverse('donations:donation_list')

class DonationsListView(generic.ListView):
    template_name = 'donations/donation_list.html'
    context_object_name = 'donation_list'
    def get_queryset(self):
        return Donation.objects.filter(
            end_date__gte=timezone.now(), 
        )

def charge(request, id):
    if request.method == 'POST':
        donation = get_object_or_404(Donation, pk=id)
        print('Data:', request.POST)
        amount = int(request.POST['amount'])
        donation.total += amount
        donation.save()

        log = UserDonation(name=donation.name, amount=amount)
        log.save()
        request.user.user_donation.add(log)

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
        return redirect(reverse('donations:success', args=[amount, donation.name, donation.total]))


def successMsg(request, arg1, arg2, arg3):
	amount, name, total = arg1, arg2, arg3
	return render(request, 'donations/success.html', {'amount':amount, 'name':name, 'total':total})

def volunteerform(request):
    form = VolunteerForm(request.POST or None)
    if form.is_valid():
        opportunity = form.save(commit = False)
        opportunity.user = request.user
        opportunity.save()
        return HttpResponseRedirect(reverse('donations:volunteer-list'))
    context = {'form': form}
    return render(request, 'donations/volunteer_post.html', context)

class UpdateVolunteerFormView(generic.UpdateView):
    model = VolunteerPost
    form_class = VolunteerForm
    template_name = 'donations/update_volunteering.html'

    def get_success_url(self):
        return reverse('donations:volunteer-list')

class DeleteVolunteerFormView(generic.DeleteView):
    model = VolunteerPost
    template_name = 'donations/delete_volunteering.html'

    def get_success_url(self):
        return reverse('donations:volunteer-list')

class VolunteerListView(generic.ListView):
    template_name = 'donations/volunteer_list.html'
    context_object_name = 'volunteer_opportunities'

    def get_queryset(self):
        return VolunteerPost.objects.filter(
            date__gte=timezone.now(), 
            # date__lte=timezone.now() + timezone.timedelta(days=100),
        )

class UserVolunteerForm(forms.ModelForm):
    class Meta:
        model= VolunteerPost
        fields = ["title", "start_time", "end_time", "date"]

def signup(request, id):
    if request.method == 'POST':
        opportunity = get_object_or_404(VolunteerPost, pk=id)

        log = UserVolunteer(title=opportunity.title, start_time=opportunity.start_time, end_time=opportunity.end_time, date=opportunity.date)
        log.save()
        request.user.user_volunteer.add(log)

        return redirect(reverse('donations:homepage'))
    return HttpResponseRedirect(reverse('donations:volunteer-list'))