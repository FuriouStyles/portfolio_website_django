from django.shortcuts import render
from django.http import HttpResponse

def notes(request):
    return render(request, 'notes/notes_home.html')
