
from django import forms

class RequestLicenseForm(forms.Form):
    last_name = forms.CharField(max_length=25, required=True)
    fist_name = forms.CharField(max_length=25, required=True)
    usufruct = forms.IntegerField(required=True) #lo que se pide
    date_form  = forms.CharField(max_length=25, required=True)
    date_to = forms.CharField(max_length=25, required=True)
    description = forms.CharField(max_length=50, required=False)
    status = forms.BooleanField(required=True)
 