from .models import toodolist
from rest_framework import serializers

class Todollist(serializers.ModelSerializer):
    class Meta:
        model = toodolist
        fields = '__all__'

        