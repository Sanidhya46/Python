from .views import get_task , update_task , delete_task , post_task
from django.urls import path, include

urlpatterns = [
     path('get_task/', get_task, name='get_task'),
    path('update_task/', update_task, name='update_task'),
    path('delete_task/', delete_task, name='delete_task'),
    path('post_task/', post_task, name='post_task'),
    
]

