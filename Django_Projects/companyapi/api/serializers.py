from rest_framework import serializers
from api.models import Company   # we are including all models of Company from api.models
from api.models import Employee
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()  # only reads not modify by api 
    class Meta:  # it stores metadata of the serializer, it tells django how the serializers should behave which models it map to 
        model = Company    
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()   
    class Meta:   
         model = Employee
         fields = "__all__"
