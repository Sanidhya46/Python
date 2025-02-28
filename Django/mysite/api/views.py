# views.py is an root that renders data on the  screen

from django.shortcuts import render   # django.shortcuts modules provides hlper function to make it easier 
from rest_framework import generics,status   # generics contain generic views update, delete extra any type of models
from rest_framework.response import Response
from .models import Blogpost
from .searializers import BlogPostSerializer
from rest_framework.views import APIView
    model = Model
    template_name = ".html"

# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):    # listcreateview is providing view, generic is class-based view provided by django rest framework that allows - i). list of all objects  ii). create a new object
    queryset = Blogpost.objects.all()   # gives all the instances
    serializer_class = BlogPostSerializer   
    
    def delete(self, request, *args, **kwargs ):  # it is own root self is an instance of class, request is http request, args recieved tuple, and kwargs recieved dicitionary (named keyword arguments)
        Blogpost.objects.all().delete()
        return Response(status=status.HTTP_204_CONTENT)      # this is an http response object from django rest framework , sends response back to the client
#  For deleting we have to create new root or we can delete using existing root
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):    # RetrieveUpdateDestroyAPIView allows you to access an individual post , update an delete
    queryset = Blogpost.objects.all()   # gives all the instances 
    serializer_class = BlogPostSerializer 
    lookup_field = "pk"    # pk stands for primary key , pk is also id of blogpost 

class BlogPostList(APIView):  # APIView is base class for all drf views , it allows you to define custom api views using (cbvs) , methods like Get, Put, Post, Delete