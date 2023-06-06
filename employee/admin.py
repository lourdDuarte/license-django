from django.contrib import admin
from employee.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin (admin.ModelAdmin):
   pass
    # list_display=[
    #     'perfil',
    #     'numerodocumento',
        
    # ]