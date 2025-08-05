
from django.urls import path

from django.urls import path , include
from expense import views

urlpatterns = [
        
    path('get-transaction/', views.get_transactions),
]
