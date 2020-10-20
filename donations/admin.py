from django.contrib import admin

from .models import Donation



class DonationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'goal', 'end_date']}),
    ]
    # inlines = [CommentInline]
    list_display = ('name', 'description', 'goal', 'end_date')
    search_fields = ['description']

admin.site.register(Donation, DonationAdmin)