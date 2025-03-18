from rest_framework import serializers
from api.models import Company   # we are including all models of Company from api.models

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  # it stores metadata of the serializer, it tells django how the serializers should behave which models it map to 
        model = Company
        fields="__all__"


     