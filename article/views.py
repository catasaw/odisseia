from django.shortcuts import render

def articles_view(request, issue_id):
    context = {}
    context['issue_id'] = issue_id
    return render(request, 'article/article_view.html', context) 
