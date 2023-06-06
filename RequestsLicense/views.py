from ast import For
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from RequestsLicense.models import RequestsLicense
from .forms import RequestLicenseForm

# Create your views here.
@login_required
def request_license(request):
    employee = request.user.profile.employee
    if request.method == 'POST':
        form = RequestLicenseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_request = RequestsLicense(employee = employee)
            new_request.last_name = data['last_name']
            new_request.fist_name = data['first_name']
            new_request.usufruct = data['usufruct']
            new_request.date_form = data['date_form']
            new_request.date_to = data['date_to']
            new_request.description = data['description']

            new_request.save()
            
       
    else:
        form = RequestLicenseForm()
    

    return render(
        request=request,
        template_name='perfil/empleado/request.html',
        context={
            'employee': employee,
            'user': request.user.profile.employee,
            'form': form
        }
    )


def  update_request(request, pk):
    license = RequestsLicense.objects.get(id=pk)
    form = RequestLicenseForm(instance=license)
    print(license)
    # if request.method == 'POST':
    #     form = RequestsLicense(request.POST, instance=license)
    #     form.save()
    #     return redirect('data')
        
    context = {'form':form}
    return render (request,'perfil/admin/view_request.html',context)

def view_request(request):
    all_request = RequestsLicense.objects.all()
    context = {'request':all_request}
    return render(
        request,
       'perfil/admin/view_request.html',
        context
    )  
        