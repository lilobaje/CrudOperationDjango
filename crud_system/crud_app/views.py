from turtle import title
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, Position
from django.urls import reverse
from django.contrib import messages

# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

def add_position(request,id=0):
    if request.method=='POST': 
        title=request.POST['title']
        add_position=Position.objects.create(title=title)
        messages.success(request,'Data has been submited')
    return render(request,"employee_register/addposition.html")

