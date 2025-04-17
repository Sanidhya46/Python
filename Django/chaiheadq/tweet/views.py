# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tweet  # Assuming you have a Tweet model
from django.http import HttpResponse

@csrf_exempt        # disables csrf (cross site request frogery) , csrf prevents unauthorised requests
def tweet_list(request):
    return HttpResponse("This is the tweet list page!")  
