from django.shortcuts import render
from api.models import Company
from rest_framework import viewsets 
from api.serializers import CompanySerializer


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):  # model viewset have all functions
    queryset = Company.objects.all()     # it retrives all object from database
    serializer_class = CompanySerializer 