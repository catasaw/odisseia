from django.http import HttpResponse
from django.shortcuts import render
from .models import Language
from django.views.generic import View


class SignupView(View):


    def get(self, request):
        languages = Language.objects.all().order_by('name')
        return render(request, 'magazine/signup.html', {'languages': languages})
        