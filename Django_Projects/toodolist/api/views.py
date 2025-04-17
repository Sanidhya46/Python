from .models import toodolist
from .serializers import  Todollist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_task(request):
    tasks = toodolist.objects.all()
    serializers = serializers(tasks, many=True)
    return Response(tasks , status=status.HTTP_200_OK )

@api_view(['POST', 'GET'])
def post_task(request):
    if request.method =='POST':
        serializer = toodolist(data= request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'GET':
        tasks = toodolist.objects.all()
        serializers = serializers(tasks, many=True)
        return Response(tasks , status=status.HTTP_200_OK )
    
@api_view(['PUT'])
def update_task(request, task_id):
    tasks = get_object_or_404(tasks, id=task_id )
    serializer = toodolist(data= request.data )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_task(request, task_id):
    tasks = get_object_or_404(tasks, id=task_id )
    tasks.delete()
    return Response(status=status.HTTP_404_NOT_FOUND)


