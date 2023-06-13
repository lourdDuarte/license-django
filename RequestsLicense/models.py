from django.db import models
from employee.models import Employee
# Create your models here.

# Create your models here.
class RequestsLicense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=25)
    fist_name = models.CharField(max_length=25)
    usufruct = models.IntegerField() #lo que se pide
    date_form = models.CharField(max_length=25)
    date_to = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)



