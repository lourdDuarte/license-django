from django.forms import ModelForm
from .models import EmployeeDetail

class FormDetail(ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'