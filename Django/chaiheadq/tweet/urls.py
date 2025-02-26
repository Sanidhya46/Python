# from . import views     # import view.py from same folder
# from django.urls import path

# urlpatterns = [
#      path('', views.index, name ='index'),
# ]

from django.urls import path
from .views import tweet_list

urlpatterns = [
    path("tweets/", tweet_list, name="tweet-list"),  # when tweet/ url is accesed then tweet_list view function will be called
]

