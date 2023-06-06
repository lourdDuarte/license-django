from math import remainder
from django.db import models
from employee.models import Employee

# Create your models here.
class EmployeeDetail(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    antiquity = models.CharField(max_length=15)
    leave_days = models.CharField(max_length=25)
    remainder = models.CharField(max_length=25)
    year = models.CharField(max_length=25)
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
def __str___(self):
    return self.employee.profile.user.username

