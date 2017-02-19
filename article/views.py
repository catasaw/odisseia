from django.shortcuts import render, redirect
from magazine.models import Article
from django.http.response import HttpResponse, HttpResponseRedirect

def article_view(request, issue_id, article_id):
    context = {}
    context['issue_id'] = issue_id
    context['article'] = article_id
    
    
    try:
        introduction=Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        
        return redirect('/')
    
    return render(request, 'article/article_view.html', {'article': introduction})
