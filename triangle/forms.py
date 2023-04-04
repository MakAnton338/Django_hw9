from django import forms
from django.forms import ModelForm, fields

from .models import PersonModels


class HypotenuseForm(forms.Form):
    a = forms.IntegerField(label='Length of leg A', min_value=1)
    b = forms.IntegerField(label='Length of leg B', min_value=1)


class PersonForm(ModelForm):
    class Meta:
        model = PersonModels
        fields = ['first_name', 'last_name', 'email']