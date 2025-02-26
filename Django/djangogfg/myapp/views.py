from django.shortcuts import render, redirect
from .models import MyModel
from .forms import MyForm

# def my_view(request):
#     if request.method == "GET":
#         return render(request, "mytemplate.html")
   # MyModel representing databasemodel
def my_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data   # expects sanitised data
            MyModel.objects.create(**data)
            return redirect('success')
        else:
            form = MyForm()  #Handling get request initial from load 

        return render(request, "mytemplate.html", {'form': form})
    
from django.http import HttpResponse

def success_view(request):
    return HttpResponse("Form submitted successfully!")
