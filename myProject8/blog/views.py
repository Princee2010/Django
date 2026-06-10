from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    students_list =[
        {"name":"Mohit", "class":"10th"},
        {"name":"Rohit", "class":"9th"},
        {"name":"Sohit", "class":"8th"},
    ]
    return render(request, 'blog/blog.html', {'students': students_list})


def about(request):
    return render(request, 'blog/about.html')
