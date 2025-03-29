from django.db import models

# Create your models here.
class todolist(models.Model):
    text = models.CharField(max_length=50)
    description = models.models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices =[
        ('completed' , 'completed'), ('pending' , 'pending') , ('startlater' , 'startlater')]
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
