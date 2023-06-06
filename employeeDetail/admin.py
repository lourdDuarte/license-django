from django.contrib import admin
from employeeDetail.models import EmployeeDetail
# Register your models here.



# Register your models here.
@admin.register(EmployeeDetail)
class EmployeeDetailAdmin (admin.ModelAdmin):
   pass
   list_display=[
        'id',
        'employee',
        
    ]