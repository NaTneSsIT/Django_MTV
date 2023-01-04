from django.shortcuts import render,redirect
from .models import employee as employee_model
from home.models import Department as department_model
# Create your views here.
def get_employee(request,id):
    employee_list=employee_model.objects.filter(department_id=id)
    department=department_model.objects.get(department_id=id)
    return render(request,'employee.html',{'employee_list':employee_list,'department':department})


def get_employee_form(request):
    department_list=department_model.objects.filter()
    return render(request,'addEmployeeForm.html',{'department_list':department_list})



def add_employee(request):
    if(request.method=="POST"):
        department_id=request.POST['department']
        name=request.POST['name']
        age=request.POST['age']
        avatar=request.FILES['avatar']
        cv=request.FILES['cv']

        departmant=department_model.objects.get(department_id=department_id)
        employee=employee_model.objects.create(department_id=departmant,
                                                name=name,
                                                age=age,
                                                avatar=avatar,
                                                cv=cv)
        employee.save()
        return redirect("/department/"+str(department_id))

    else:
        return render(request,'error.html')

def get_Editemployee_form(request):
    department_list=department_model.objects.filter()
    return render(request,'editEmployeeForm.html',{'department_list':department_list})

def edit_employee(request):
    if(request.method=="POST"):
        employee_id=request.POST['id']
        department_id=request.POST['department']
        name=request.POST['name']
        age=request.POST['age']
        avatar=request.FILES['avatar']
        cv=request.FILES['cv']
        departmant=department_model.objects.get(department_id=department_id)
        employeeTMP=employee_model.objects.get(employee_id=employee_id)
        employeeTMP.department_id=departmant
        employeeTMP.name=name
        employeeTMP.age=age
        employeeTMP.avatar=avatar
        employeeTMP.cv=cv
        employeeTMP.save()
        return redirect("/department/"+str(department_id))

    else:
        return render(request,'error.html')  

def get_employeeDEL_form(request):
    return render(request,'deleteEmployeeForm.html')

def delete_employee(request):
    if(request.method=="POST"):
        employee_id=request.POST['id']
        employeeTMP=employee_model.objects.get(employee_id=employee_id)
        department_id=employeeTMP.department_id.department_id
        employeeTMP.delete()
        return redirect("/department/"+str(department_id))
    else:
        return render(request,'error.html')