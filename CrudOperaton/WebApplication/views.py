from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from WebApplication.forms import GovernmentEmployeeForm
from WebApplication.models import GovernmentEmployee

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'WebApplication/SuperAdminNavbar.html')
        else:
            messages.error(request, 'Username or password incorrect')
    return render(request, 'WebApplication/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../login/')


def addGovtEmployee(request):
    if request.method == "POST":
        form = GovernmentEmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('viewGovtEmployee')
            except:
                pass
    else:
        form = GovernmentEmployeeForm()
    return render(request,'WebApplication/GovernmentEmployeeInsert.html',{'form':form})
def viewGovtEmployee(request):
    governmentEmployees = GovernmentEmployee.objects.all()
    return render(request,"WebApplication/GovernmentEmployeeShow.html",{'governmentEmployees':governmentEmployees})

def editGovtEmployee(request,GovernmentEmployeeID):
    governmentEmployee = GovernmentEmployee.objects.get(GovernmentEmployeeID=GovernmentEmployeeID)
    return render(request,'WebApplication/GovernmentEmployeeEdit.html', {'governmentEmployee':governmentEmployee})

def updateGovtEmployee(request, GovernmentEmployeeID):
    governmentEmployee = GovernmentEmployee.objects.get(GovernmentEmployeeID=GovernmentEmployeeID)
    form = GovernmentEmployeeForm(request.POST, instance = governmentEmployee)
    if form.is_valid():
        form.save()
        return redirect("viewGovtEmployee")
    return render(request, 'WebApplication/GovernmentEmployeeEdit.html', {'governmentEmployee': governmentEmployee})

def deleteGovtEmployee(request, GovernmentEmployeeID):
    student = GovernmentEmployee.objects.get(GovernmentEmployeeID=GovernmentEmployeeID)
    student.delete()
    return redirect("viewGovtEmployee")
