from django.contrib import admin
from django.urls import path , include

from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers


# roputer providing everything to handle viewsets 
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls)),    # you can given all the company urls
      # we are just passing the reference of it 

]

# if we want particular url company{companyid}/employees
