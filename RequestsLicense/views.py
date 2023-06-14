from ast import For
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from RequestsLicense.models import RequestsLicense
from .forms import RequestLicenseForm
import yagmail
from datetime import date

date = date.today()
# Create your views here.
@login_required
def request_license(request):
    form = RequestLicenseForm()
    if request.method == 'POST':
        form = RequestLicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render (request,'perfil/empleado/request.html',{'form':form})
    
   


@login_required
def  update_request(request, pk):
    detail = RequestsLicense.objects.get(id=pk)
    correo = detail.employee.profile.user.email
    form = RequestLicenseForm(instance=detail)
    if request.method == 'POST':
        form = RequestLicenseForm(request.POST, instance=detail)
        comentario = request.POST['comentario']
        if form.is_valid():

            form.save()
            print(comentario)
            send_email(correo,comentario)
            return redirect('request')
        
    context = {'form':form}
    return render (request,'perfil/admin/update_license.html',context)

def delete_request(request, pk):
    request = RequestsLicense.objects.get(id=pk)
    request.delete()
    return redirect('request')


@login_required
def view_request(request):
    all_request = RequestsLicense.objects.all()
    context = {'all_request': all_request}
    return render(
        request,
       'perfil/admin/view_request.html',
        context
    )  


def send_email(destinario, msj):
    password = 'badspsaurjkgkxvj'
    email = 'lourdes123duarte@gmail.com'
    yag = yagmail.SMTP(user = email, password = password)
    destinario = [destinario]
    asunto = 'SOLICITUD DE LICENCIA'
    mensaje = msj
    yag.send(destinario,asunto, mensaje)

@login_required
def dashboard_admin(request):

    people_on_vacation = RequestsLicense.objects.filter(status = 1, date_to__gt = date).order_by('fecha_actualizacion')
    context = {'adm':people_on_vacation}

    
    return render(request, 'perfil/admin/dashboard_admin.html', context)
