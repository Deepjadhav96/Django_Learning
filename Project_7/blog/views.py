from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
def home(request):
    context = {
        "name":"Deep Jadhav",
        "age":25,
        "skills":["Python","Django","React"],
        "user":User("Kumar",30),
        "blog":{
            "title":"Django Template Intro",
            "content":"<b>This is bold</b>",
            "Created_at":datetime(2026,11,20,11,50)
        },
        "empty_value":"None",
    }

    return render(request,"blog/home.html",context)