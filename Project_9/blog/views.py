from django.shortcuts import render
from datetime import datetime
# Create your views here.

def blog_list(request):
    blogs = [
        {"title":"Django Basics","is_featured":True,"author":"Mohit Kumar"},
        {"title":"Django Advanced","is_featured":False,"author":""},
        {"title":"Django REST Framework","is_featured":False,"author":"Dr. Ajay Mittal"},
    ]
    context = {
        "blogs": blogs,
        "today":datetime.now(),
        "html_code":"<b> Welcome to My Blog </b>",
    }
    return render(request,'blog/home.html',context)