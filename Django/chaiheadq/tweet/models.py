from django.db import models

# Create your models here.
from django.db import models

class Tweet(models.Model):      # new class named tweet which is database table , models.Model means python built in .. which provide functionalities for database interaction
    text = models.TextField()   
    created_at = models.DateTimeField(auto_now_add=True)  # stores the timestamp when tweet is created
