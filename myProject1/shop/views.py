from django.http import HttpResponse
# Create your views here.
def home (request):
    return HttpResponse("Hello, World! This is the home page of the shop.")

def products (request):
    return HttpResponse("This is the products page of the shop. Here you can find all our available products.")
# Create your views here.
