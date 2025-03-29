from .models import todolist
from rest_framework import serializers

class toodolistserializer(serializers.ModelSerializer):
    class Meta:
      Model = todolist
      fields =  '__all__'

