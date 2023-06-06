from django.db import models
from profile.models import Profile

# Create your models here.
class Employee(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    document_number = models.CharField(max_length=25, blank=False)
    admission_date = models.DateField()


def __str__(self):
    return self.profile.user.username

