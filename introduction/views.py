from django.shortcuts import render, redirect
from magazine.models import Introduction
from django.http.response import HttpResponse, HttpResponseRedirect

def introduction_view(request, issue_id, introduction_id):
    context = {}
    context['issue_id'] = issue_id
    context['introduction'] = issue_id
    
    
    try:
        introduction=Introduction.objects.get(id=introduction_id)
    except Introduction.DoesNotExist:
        
        return redirect('/')
    
    return render(request, 'introduction/introduction_view.html', {'introduction': introduction})
