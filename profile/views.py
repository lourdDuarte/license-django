import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from profile.models import Profile
from employee.models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash



# Create your views here.
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard_admin')
            else:
                return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username and password'})

    return render(request, 'login.html')
   


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confimation = request.POST['password_confirmation']
        document_number = request.POST['document_number']
        admission_date = request.POST['admission_date']
        if password != password_confimation:
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden'})
        
        try:
            user = User.objects.create_user(username = username, password= password)
        except:
            return render(request, 'register.html', {'error': 'Usuario existente'})

        user.last_name = last_name
        user.first_name = first_name
        user.email = email
        
        user.save()

        profile = Profile(user = user)
        
        profile.save()

        employee = Employee(profile = profile)
        employee.document_number = document_number
        employee.admission_date = admission_date

        employee.save()

        return redirect('login')
        
    return render (request,'register.html')

def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        redirect('dashboard')
    return render (request, 'profile.html', {'form':form})




def logout_view(request):
    logout(request)
    return redirect('login')