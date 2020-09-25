from django.http import HttpResponse

from django.views import generic

from .models import Donation


def index(request):
    return HttpResponse("Welcome to the Donations Page!")

class DonationView(generic.ListView):
    template_name = 'donations/navbar.html'

    def get_queryset(self):
        return Donation.objects.all()