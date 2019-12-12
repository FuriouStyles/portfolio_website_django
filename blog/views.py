from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


posts = [
    {
        'author': "Stephen Plainte",
        "title": "My Example Blog Post",
        "content": "This is the body of my first blog post.",
        "date_posted": datetime.now().strftime("%d-%b-%Y")
    },
    {
        'author': "Stephen Plainte",
        "title": "My Second Example Blog Post",
        "content": "This is the body of my second example blog post, ever so different from the first.",
        "date_posted": datetime.now().strftime("%d-%b-%Y")
    }
]

def blog(request):
    context = {
        'posts': posts,
        'title': "Blog"
    }
    return render(request, 'blog/blog.html', context)

def about(request):
    context = {
        'title': 'About Me'
    }
    return render(request, 'blog/about.html', context)

def homepage(request):
    return render(request, 'blog/home.html')
