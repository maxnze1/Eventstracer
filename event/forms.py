from django import forms
from .models import EventPage
from dal import autocomplete


class EventSearchForm(forms.ModelForm):
    class Meta:
        model = EventPage
        fields = ('__all__')
        widgets = {
            'title': autocomplete.ModelSelect2(url='event-autocomplete')
        }
