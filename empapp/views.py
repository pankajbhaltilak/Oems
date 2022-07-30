from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def allemp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'allemp.html',context)


def addemp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = request.POST['salary']
        bonus =int(request.POST['bonus'])
        phone =int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp= Employee(firstname=firstname, lastname=lastname,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hiredate=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method =='GET':
        return  render(request,'addemp.html')
    else:
        return HttpResponse('An exception occured ! Employee')


def removeemp(request ,emp_id=0):
    if emp_id:
        try:
            emptoberemoved = Employee.objects.get(id=emp_id)
            emptoberemoved.delete()
            return HttpResponse('Employee removed successfully')
        except:
            return HttpResponse("Please Enter a Valid Emoloyee ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'removeemp.html', context)


def filteremp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(firstname__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains= dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context ={
            'emps':emps
        }
        return render(request,'allemp.html',context)

    elif request.method == 'GET':
        return render(request,'filteremp.html')
    else:
        return HttpResponse('An Exception')
