from django.contrib import admin
from .models import employee

# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display=("employee_id","department_id","name","age","avatar","cv")
    search_fields=['name']
    list_filter=('employee_id','department_id','name','age')

admin.site.register(employee,employeeAdmin)