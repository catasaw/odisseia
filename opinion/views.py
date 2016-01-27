from django.shortcuts import render, redirect
from magazine.models import Opinion, Opinion_Vote
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from opinion.opinionform import OpinionForm
from django.http.response import HttpResponseRedirect
from django.template.context_processors import csrf

@login_required
@csrf_protect
def opinions_view(request, issue_id):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = Opinion.objects.create(
            content=form.cleaned_data['content'],
            contributor=request.user,
            issue_id = issue_id,
            language = form.cleaned_data['language']
            )
            return redirect('issue_view', issue_id = issue_id)  
    else:
        form = OpinionForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form
    
    # TODO: Order by most positive votes
    # TODO: Write this in a Manager?
    all_opinions = Opinion.objects.filter(issue_id=issue_id).order_by('-created_at')
    context['opinions'] = all_opinions
    return render(request, 'opinion/opinion_view.html', context)

@login_required
def vote_view(request, issue_id, opinion_id, vote_type):
    # TODO: REFACTOR vote. Check if opinion and issue exist and correspond
    vote = 1
    
    if vote_type == 'down':
        vote = -1
        
    new_vote = Opinion_Vote.objects.create(
    issue_id = issue_id,
    opinion_id = opinion_id,
    contributor=request.user,
    vote = vote,     
    )
    
    # TODO: Double check if redirect is ok
    return redirect('opinions_view', issue_id = issue_id)