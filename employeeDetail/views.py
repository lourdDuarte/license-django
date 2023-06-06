from ast import For
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee.models import Employee
from employeeDetail.models import EmployeeDetail
from .forms import FormDetail

# Create your views here.
@login_required
def search_datail(request):
    employee = Employee.objects.all()
    context = {'employee':employee}

    if request.method == 'POST':
        empleado = request.POST['employee']
        print ("********************"+ empleado + "**************************")
        detail = EmployeeDetail.objects.all().filter(employee=empleado).order_by('year')
        context_detail = {'detail':detail}
        context.update(context_detail) #update context
        
        

    return render (request,'data/data_licenses.html',context)


@login_required
def update_detail(request,pk):

   detail = EmployeeDetail.objects.get(id=pk)

   form = FormDetail(instance=detail)
  
   if request.method == 'POST':
        form = FormDetail(request.POST, instance=detail)
        form.save()
        return redirect('data')
        
   context = {'form':form}
   return render (request,'data/update_detail.html',context)

@login_required
def add_detail(request):
    employee = request.user.profile.employee
    all_employee = Employee.objects.all()
    
    if request.method == 'POST':
        form = FormDetail(request.POST)
        if form.is_valid:
            form.save()
            return redirect('data')

    context = {'detail':all_employee}
    return render (request,'data/new_detail.html',context)

@login_required
def new_detail(request):
    employee = Employee.objects.all()
    context = {'employee':employee}
    return render(request, 'data/new_detail.html', context)