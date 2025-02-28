# searilizers defines class that takes data from models and converted into json compatable data through which you can interact with api
from django.shortcuts import render   # django.shortcuts modules provides hlper function to make it easier 
from rest_framework import serializers   # generics contain generic views update, delete extra any type of models
from .models import Blogpost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ["id","title","content","published_date"]