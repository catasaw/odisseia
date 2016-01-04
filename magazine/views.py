from django.shortcuts import render
from django.http import HttpResponse
from .models import Opinion,Article

def homepage(request):
    return render(request, 'magazine/homepage.html')