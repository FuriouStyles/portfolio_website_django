from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('<h1>About Me</h1>')

def home(request):
    return HttpResponse("<h1>Stephen's Homepage</h1>")
