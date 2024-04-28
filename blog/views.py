from django.shortcuts import render # type: ignore
from django.http import HttpResponse

# Create your views here.

def my_blog(request):
    return HttpResponse("Hello, Blog!")