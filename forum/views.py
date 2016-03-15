from django.shortcuts import render, render_to_response, redirect
from magazine.models import Issue, Comment, Issue_Contributor
from forum.commentform import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@csrf_protect
@login_required
def issue_view(request, issue_id):   
    try: 
        issue=Issue.objects.get(pk=issue_id)
    except Issue.DoesNotExist:
        return HttpResponseRedirect('/dashboard/') 
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():    
            comment = Comment.objects.create(
            content=form.cleaned_data['content'],
            contributor=request.user,
            issue_id = issue_id
            )
            return redirect('issue_view', issue_id = issue_id) 
    else:
        form = CommentForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    all_comments = Comment.objects.filter(issue_id=issue_id).order_by('-created_at')
    token['comments'] = all_comments
    token['issue'] = issue
    token['contributors'] = issue.issue_contributors.all()
    
    # TODO: Don't access database every time that comment is post it. Split functionality
    token['is_contributor'] = True
    try:
        issue_contributor=Issue_Contributor.objects.get(issue_id=issue_id, contributor_id= request.user.id)
    except Issue_Contributor.DoesNotExist:
        token['is_contributor'] = False  
        
    return render(request, 'forum/issue_view.html', token)
