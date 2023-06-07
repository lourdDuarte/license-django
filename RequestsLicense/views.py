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
    all_request = RequestsLicense.objects.all()
    
    if request.method == 'POST':
        form = RequestLicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil/empleado/request.html')

    context = {'detail':all_request}
    return render (request,'perfil/empleado/request.html',context)
    
   


@login_required
def  update_request(request, pk):
    detail = RequestsLicense.objects.get(id=pk)

    form = RequestLicenseForm(instance=detail)
    if request.method == 'POST':
        form = RequestLicenseForm(request.POST, instance=detail)
        comentario = request.POST['comentario']
        if form.is_valid():
            form.save()
            print(comentario)
            return redirect('request')
        
    context = {'form':form}
    return render (request,'perfil/admin/update_license.html',context)


@login_required
def view_request(request):
    all_request = RequestsLicense.objects.all()
    context = {'request':all_request}
    return render(
        request,
       'perfil/admin/view_request.html',
        context
    )  

