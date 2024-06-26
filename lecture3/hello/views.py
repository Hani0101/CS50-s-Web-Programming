from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def hani(request):
    return HttpResponse("Hello, Hani!")

def sunbul(request):
    return HttpResponse("hello, Subnbul!")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name":name.capitalize()
    })
