from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.my_view, name ='home'),
    path('success/', lambda request: HttpResponse("Success! This is the view output.") , name = 'success')
]