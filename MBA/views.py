from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'mba/home.html')

def about(request):
    return render(request,'mba/about.html')