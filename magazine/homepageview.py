from django.http import HttpResponse
from django.shortcuts import render
from .models import Opinion,Article,Issue
from django.views.generic import View

class HomepageView(View):


    def get(self, request):
        last_issue = Issue.objects.latest('published_at')
        return render(request, 'magazine/homepage.html', {'issue': last_issue})
        