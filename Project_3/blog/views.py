from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def post_details(request,post_id):
    return HttpResponse(f"<h1>Show Blog post : {post_id}</h1>")

def user_profile(request,username):
    return HttpResponse(f"<h1>Profile of user : {username}</h1>")

def articles_by_year(request,year):
    return HttpResponse(f"<h1>Articles from the year {year}</h1>")

def article_details(request,year,month):
    return HttpResponse(f"<h1>Article from {year} - {month}</h1>")