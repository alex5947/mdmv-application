from django.contrib import admin

from .models import Donation, VolunteerPost, UserDonation



class DonationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'goal', 'end_date']}),
    ]
    # inlines = [CommentInline]
    list_display = ('name', 'description', 'goal', 'end_date')
    search_fields = ['description']

class UserDonationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'amount']}),
    ]
    # inlines = [CommentInline]
    list_display = ('name', 'amount')
    search_fields = ['name']

admin.site.register(Donation, DonationAdmin)
admin.site.register(UserDonation, UserDonationAdmin)

class VolunteerPostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('title', 'date', 'start_time', 'end_time', 'description')})
    ]

admin.site.register(VolunteerPost, VolunteerPostAdmin)
