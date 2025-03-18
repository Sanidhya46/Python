from django.db import models

# Create your models here.

#creating company model 
class Company(models.Model):  #models.Model is from object relation mapper which create database models
    company_id = models.AutoField(primary_key=True)  # we are defining this for own primary key 
    name = models.CharField(max_length=50)  # creating models for character field of max_length 50 to name 
    location = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    type = models.CharField( max_length=50,choices = (('IT','IT'),
                                                      ('Non IT', 'Non IT'), 
                                                      ('Mobile Phones','Mobile Phones')
                                                      ))
    added_date = models.DateTimeField(auto_now=True)  # It stores the time when your object is modified
    active = models.CharField(default=True)   #If no values is specified during object creation 

#Employee model 