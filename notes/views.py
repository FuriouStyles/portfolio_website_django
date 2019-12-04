from django.shortcuts import render
from django.http import HttpResponse

def notes(request):
    return HttpResponse('<h1>Class Notes</h1>')
