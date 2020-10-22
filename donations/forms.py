from .models import VolunteerPost
from django import forms

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerPost
        fields = ('title', 'name', 'date', 'start_time', 'end_time', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Rake Leaves'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'xx/xx/20xx'}),
            'start_time' : forms.TimeInput(attrs={'class': 'form-control', 'placeholder': '00:00-23:59'}),
            'end_time' : forms.TimeInput(attrs={'class': 'form-control', 'placeholder': '00:00-23:59'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job description here...'}),
        }