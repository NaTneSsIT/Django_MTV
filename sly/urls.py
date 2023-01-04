"""sly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from employee import views as views_em
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.get_home),
    path('department/<int:id>/',views_em.get_employee),
    path('addEmployeeForm/',views_em.get_employee_form),
    path('addEmployee',views_em.add_employee),
    path('editEmployeeForm/',views_em.get_Editemployee_form),
    path('editEmployee',views_em.edit_employee),
    path('deleteEmployeeForm/',views_em.get_employeeDEL_form),
    path('deleteEmployee',views_em.delete_employee)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_header="SLY IN PART OF YOUR LIFE <3"