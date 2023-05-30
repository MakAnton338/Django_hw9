from django import forms


class SmsModel(forms.Form):
    phone_number = forms.IntegerField(label='Wrote a phone number', min_value=1)
