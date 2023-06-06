import email
from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    username = forms.CharField(max_length=15, required=True)
    email = forms.CharField(max_length=30, required=True)
