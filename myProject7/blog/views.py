from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_list(request):
    blogs = [
        {
            "title":"First Blog",
            "is_featured":True,
            "author":"John Doe",
            "content":"This is the content of the first blog.",
            "created_at":datetime(2024,6,1,10,0)
        },
        {
            "title":"Second Blog",
            "is_featured":False,
            "author":"mohan Doe",
            "content":"This is the content of the second blog.",
            "created_at":datetime(2024,6,2,12,0)
        },
        {
            "title":"Third Blog",
            "is_featured":False,
            "author":"Alice Smith",
            "content":"This is the content of the third blog.",
            "created_at":datetime(2024,6,3,14,0)
        }
    ]
    context ={
        "blogs":blogs,
        "today" :datetime.now(),
        "html_code":"<h1>This is a heading</h1>",
    }
    return render(request,"blog/blog_list.html",context)
