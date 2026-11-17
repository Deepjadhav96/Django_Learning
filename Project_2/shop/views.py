from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return HttpResponse("Home page of shop app")

def about(request):
    return HttpResponse("About page of shop app")