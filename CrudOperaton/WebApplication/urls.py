"""CrudOperaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from WebApplication import views

urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addGovtEmployee', views.addGovtEmployee, name='addGovtEmployee'),
    path('viewGovtEmployee', views.viewGovtEmployee, name='viewGovtEmployee'),
    path('editGovtEmployee/<int:GovernmentEmployeeID>', views.editGovtEmployee, name='editGovtEmployee'),
    path('updateGovtEmployee/<int:GovernmentEmployeeID>', views.updateGovtEmployee, name='updateGovtEmployee'),
    path('deleteGovtEmployee/<int:GovernmentEmployeeID>', views.deleteGovtEmployee, name='deleteGovtEmployee'),
]
