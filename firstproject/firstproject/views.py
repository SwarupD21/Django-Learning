from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World....This is my first Django Project")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello World....I am Swarup")

def contact(request):
    return HttpResponse("Hello World....This is my contact")