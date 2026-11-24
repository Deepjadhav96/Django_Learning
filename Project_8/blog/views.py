from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_details(request):

    post = {
        "Title":"My second templates post",
        "Description":"I'm Learning django web framework",
        "Author":"Yes",
        "Created_at":datetime(2026,11,21,14,00),
        "Comments_count": 5,
        "Tags":["Django","Python","Java","Spring-Boot"],
        "Price":100,
        "Number":50
    }

    return render(request,'blog/blog_details.html',{"post":post})