# myapp/views.py

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, world!")


def products(request):
    return HttpResponse("products")


def home(request):
    return HttpResponse("home")


def organic(request):
    return HttpResponse("organic")
