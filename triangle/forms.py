from django import forms


class HypotenuseForm(forms.Form):
    a = forms.IntegerField(label='Length of leg A', min_value=1)
    b = forms.IntegerField(label='Length of leg B', min_value=1)