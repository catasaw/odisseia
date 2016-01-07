from django.shortcuts import render, render_to_response, redirect
from magazine.models import Issue, Comment
from forum.commentform import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

@csrf_protect
def issueview(request, issue_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save()
            return redirect('issue-view', issue_id = issue_id) 
    else:
        form = CommentForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    all_comments = Comment.objects.all().order_by('created_at')
    token['comments'] = all_comments   
    return render_to_response('forum/issue_view.html', token)
    
