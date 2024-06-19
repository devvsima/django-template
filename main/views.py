from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request) -> HttpResponse:
    context = {
        "title": 'Name',
    }
    return render(request, 'main/index.html', context)
