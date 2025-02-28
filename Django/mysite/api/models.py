from django.db import models

# Create your models here.
# class blogpost(models.Model):
#     title = models.CharField(max_length = 100)   # title is field attributes, models.CharField is field type
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_add_now = True)

#     def __str__(self):        # str is an special method that defines how an object should be represented in a string , this  defines str method for the model
#         return self.title     # this returs title field of an string representation

class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  
    published_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title