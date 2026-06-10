from django.http import HttpResponse    

# Create your views here.

def post_detail(request,post_id):
    return HttpResponse(f"<h1>Show blog post {post_id}</h1>")

def user_profile(request,username):
    return HttpResponse(f"<h1>Show user profile {username}</h1>")

def article_by_year(request,year):
    return HttpResponse(f"<h1>Show articles from the year {year}</h1>")

# def article_detail(request,year,month):
#     return HttpResponse(f"<h1>Show article from {year}-{month}</h1>")

def article_detail(request, **kwargs): 
    return HttpResponse(f"<h1>Show article from {kwargs}</h1>")