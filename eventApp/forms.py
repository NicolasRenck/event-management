from django import forms
from .models import Events
from .models import Ticket
from django.forms import ClearableFileInput

class EventForm(forms.ModelForm):
    starts_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Events
        fields = ['nameEvent', 'description', 'starts_at', 'image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'image-upload'})
        }




class TicketForm(forms.Form):
    full_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)