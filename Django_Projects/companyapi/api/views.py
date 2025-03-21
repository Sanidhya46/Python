from django.shortcuts import render
from api.models import Company , Employee
from rest_framework import viewsets 
from api.serializers import CompanySerializer , EmployeeSerializer


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):  # model viewset have all functions
    queryset = Company.objects.all()     # it retrives all object from database
    serializer_class = CompanySerializer 

#what if we have to making custom urls for company id/employees
# so we have to get own pk
    def employees(self,request,pk=None): # primary key means it get primary key of company
        pass   #self - current class of an object  , request - data of an object , pkk = None means primary key
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer