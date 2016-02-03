from django.shortcuts import render
from django.http import HttpResponse
from .models import Opinion,Article,Issue

def homepage(request):
    last_issue = Issue.objects.latest('status_changed_at')
    return render(request, 'magazine/homepage.html', {'issue': last_issue})