from django.shortcuts import render
from rest_framework.decorators import api_view
from models import todolist
from serializer import toodolistserializer
# Create your views here.

@api_view('GET') #server want to see data
def showtask(request):
    task = todolist.objects.all()  # on making request it starts fethcing all objects from models
    serialize = toodolistserializer()



