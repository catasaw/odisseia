from django.shortcuts import render, redirect
from magazine.models import Opinion, Opinion_Vote
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from opinion.opinionform import OpinionForm
from django.http.response import HttpResponseRedirect
from django.template.context_processors import csrf
from django.db.models import Sum
from django.db.models.expressions import Case
from django.utils.translation import gettext as _

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
    context['contributor_id'] = request.user.id
    
    # TODO: Order by most positive votes
    # TODO: Write this in a Manager?
    all_opinions = Opinion.objects.filter(issue_id=issue_id).order_by('-created_at').select_related().all()                                                                                    
    context['opinions'] = all_opinions
    return render(request, 'opinion/opinion_view.html', context)

@login_required
def vote_view(request, issue_id, opinion_id, vote_type):
    # Check if the contributor is still allowed to vote.
    # A contributor can only use 5 votes
    # Once a vote is used, it cannot be 
    # TODO: REFACTOR vote. Check if opinion and issue exist and correspond
    
    vote = 1
    
    if vote_type == 'down':
        vote = -1
        
    # Check if contributor has voted already this vote_type on that issue
    amount_vote_type = Opinion_Vote.objects.filter(opinion_id = opinion_id).filter(contributor_id = request.user.id).filter(vote = vote).count()
    
    if (amount_vote_type > 0):
        return render(request, 'opinion/invalid_vote_view.html', {'message': _('You have already voted for this opinion!',)})
    
    # Check if contributor has voted opposite in that opinion
    opposite_votes = Opinion_Vote.objects.filter(opinion_id = opinion_id).filter(contributor_id = request.user.id).filter(vote = (-1)* vote)
    
    if opposite_votes:
        opposite_votes[0].delete()
    else:
        # Check if contributor is allowed to vote: If it has more than 5 votes
        amount_contributor_votes = Opinion_Vote.objects.filter(opinion_id = opinion_id).filter(contributor_id = request.user.id)
        if len(amount_contributor_votes) < Opinion_Vote.MAX_VOTES_PER_CONTRIBUTOR:
            # Make new vote
            new_vote = Opinion_Vote.objects.create(
            issue_id = issue_id,
            opinion_id = opinion_id,
            contributor=request.user,
            vote = vote,     
            )
        else:
            return render(request, 'opinion/invalid_vote_view.html', {'message': _('You have voted more than 5 times! Please, remove one of your votes to vote again!',)})
        
    
    # TODO: Double check if redirect is ok
    return redirect('opinions_view', issue_id = issue_id)