from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django_select2.forms import Select2MultipleWidget

from .models import Venue

class VenueCreateForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'secondary_names', 'description', 'categories',
                  'position', 'phone_number', 'web', 'schedules', 'valet_parking',
                  'auto_service', 'wifi', 'restrooms', 'credit_cards', 'reservations',
                  'outdoor_seats', 'air_conditioning', 'parking', 'delivery', 'to_take_away',
                  'wheelchair_access']
        widgets = {
            'categories': Select2MultipleWidget(),
            'description': forms.Textarea(attrs={'rows': "3"}),
            'secondary_names': forms.Textarea(attrs={'rows': "3"}),
        }