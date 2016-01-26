from django.shortcuts import render

def opinions_view(request, issue_id):
    context = {}
    context['issue_id'] = issue_id
    return render(request, 'opinion/opinion_view.html', context) 
