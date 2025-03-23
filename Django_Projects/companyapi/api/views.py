from django.shortcuts import render
from api.models import Company , Employee
from rest_framework import viewsets 
from api.serializers import CompanySerializer , EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):  # model viewset have all functions
    queryset = Company.objects.all()     # it retrives all object from database
    serializer_class = CompanySerializer 

#what if we have to making custom urls for 
# so we have to get own pk means companyViewSet
#company id/{companyId}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None): # primary key means it get primary key of company
        try:
        
            company = Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps,many=True,context={'request' : request})
            return Response(emps_serializer.data)   # we serialize because we have to send in json 
        except Exception as r:
            print(r)
            return Response({
                'message' : 'Company might not exist '
            })
        pass #pass is an prevents holder which prevents errors wheen a function has no implentation  #self - current class of an object  , request - data of an object , pkk = None means primary key
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer