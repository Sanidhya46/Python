# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tweet  # Assuming you have a Tweet model

@csrf_exempt
def tweet_list(request):
    if request.method == "GET":
        tweets = list(Tweet.objects.values())  # Convert QuerySet to list
        return JsonResponse(tweets, safe=False)
