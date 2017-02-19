from django.shortcuts import render, redirect
from magazine.models import Article, Article_Translation
from django.http.response import HttpResponse, HttpResponseRedirect

def article_view(request, issue_id, article_id):
    context = {}
    context['issue_id'] = issue_id
    context['article'] = article_id
    
    article_translation = Article_Translation.objects.filter(article_id = article_id).filter(language_to__iso1_code = request.LANGUAGE_CODE).first()
    if article_translation:
        return render(request, 'article/article_view.html', {'article': article_translation})
    
    # If there is no translation, display original
    try:
        article= Article.objects.get(id=article_id)
        return render(request, 'article/article_view.html', {'article': article}) 
    except Article.DoesNotExist:
        return redirect('/') 
            