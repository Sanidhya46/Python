from django.contrib import admin
from django.urls import path , include

from api.views import CompanyViewSet
from rest_framework import routers

# roputer providing everything to handle viewsets 
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
urlpatterns = [
    path('', include(router.urls)),    # you can given all the company urls
      # we are just passing the reference of it 

]
