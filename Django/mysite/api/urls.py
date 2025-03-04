from django.urls import path
from . import views    # importing views for using them

urlpatterns = [
    path("blogpost/", views.BlogPostListCreate.as_view(),name="blogpost-view-create"),
    path("blogpost/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(),  # when u hit url then u r able to update delete and retrive
         name = "update",  # give unique identifier and makes url change easier 
         ),
]
