from pyexpat import model
from django.contrib import admin
from RequestsLicense.models import RequestsLicense
# Register your models here.

@admin.register(RequestsLicense)
class RequestLicensesAdmin(admin.ModelAdmin):
    pass
