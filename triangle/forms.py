from django import forms


class HypotenuseForm(forms.Form):
    a = forms.FloatField(label='Length of leg A')
    b = forms.FloatField(label='Length of leg B')