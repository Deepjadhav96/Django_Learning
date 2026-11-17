from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse("Welcome to the blog app")

def about(request):
    return HttpResponse("About page of the Blog App")

def articles_by_year(request,year):
    return HttpResponse(f"<h1>Articles from the year {year}</h1>")
