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
                                                      ('Mobile Phones','Mobile Phones'),
                                                      ('Software Engineers','Soft')
                                                      ))
    added_date = models.DateTimeField(auto_now=True)  # It stores the time when your object is modified
    active = models.CharField(max_length=50,default=True)   #If no values is specified during object creation 




#Employee model 

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('manager', 'manager'),
        ('software engineer','software engineer'),
        ('Project manager','Pl')
    ))

    # In company there can be many employee model so we are going to use primary key one to many 
    # if you are writing inside other class then each instance of this model is linked with single instance of company
    # Foreign key comes from the company class
    company = models.ForeignKey(Company,on_delete=models.CASCADE)