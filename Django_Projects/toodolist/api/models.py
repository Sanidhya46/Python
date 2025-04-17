from django.db import models

class toodolist(models.Model):
    text = models.CharField(max_length='50')
    description = models.CharField(max_length='100')
    status = models.CharField(max_length='50', choices= (
        ('pending', 'pending') , ('completed' , 'completed') ,('processing ', 'processing')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    
