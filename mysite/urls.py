
##django
from unicodedata import name
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# polls
from profile import views as pf
from employee import views as emp
from RequestsLicense import views as license
from employeeDetail import views as detail


urlpatterns = [
    # vistas generales
    path('admin/', admin.site.urls),
    path ('users/login/', pf.login_view, name='login'),
    path('signup/',pf.signup_view, name='signup'),
    path('logout/', pf.logout_view, name = 'logout'),
    path(
        'change-password/',
        pf.change_password,
        name='change_password'
    ),
    # vistas sin acceso de admin
    path('dashboard/', emp.dashboard_view, name='dashboard'),
    path('solicitud/', license.request_license, name='request_license'),
    path('profile/',emp.update_profile,name="update_profile"),
    path('load-data/', detail.search_datail, name='data'),
    path('update-detail/<str:pk>/', detail.update_detail, name="update-detail"),
    path('update-request/<str:pk>/', license.update_request, name="update-request"),
    path('new-detail/', detail.add_detail,name='new_detail'),
    # vistas admin
    path('dashboard_admin/', pf.dashboard_admin, name='dashboard_admin'),
    path('request/',  license.view_request, name='request')
 

] 