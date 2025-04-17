from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_transactions(request):
    queryset = Transactions.objects.all()
    serializer = TransactionSerializer(queryset, many =True)
    return Response({
        "data" : serializer.data 
    })
