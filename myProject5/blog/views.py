from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

def home(request):
    context={
        "name":"Princee",
        "age":19,
        "skills":["Python","JavaScript","Django"],
        "user":User("Alice",25),
        "blog":{
            "title":"My First Blog Post",
            "content": "<b>This is the content of my first blog post.</b>",
            "created_at": datetime(2025,8,18,10,30),
        },
        "empty_value": None
    }
    return render(request,"blog/home.html",context)


#filters

def blog_detail(request):
    post={
        "title":"My Second Blog Post",
        "description": "<b>This is the content of my second blog post.</b>",
        "author": None,
        "created_at": datetime(2025,8,25,10,30),
        "comments_count": 5,
        "tags": ["django", "python", "web development"],
        "image_url": "https://example.com/image.jpg",
        "price": 100,
        "number" : 789,
    }
    return render(request,"blog/blog_detail.html",{"post":post})