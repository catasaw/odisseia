from django.shortcuts import render, redirect
from magazine.models import Opinion, Opinion_Vote, Issue
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from opinion.opinionform import OpinionForm
from django.http.response import HttpResponseRedirect
from django.template.context_processors import csrf
from django.db.models import Sum
from django.db.models.expressions import Case
from django.utils.translation import gettext as _
from django.db.models.aggregates import Count
from datetime import date, datetime

@login_required
@csrf_protect
def opinions_view(request, issue_id):
    context = {}
    context.update(csrf(request))
    context['contributor_id'] = request.user.id
    context['issue_id'] = issue_id
    
    # TODO: Order by most positive votes
    # TODO: Write this in a Manager?
    all_opinions = Opinion.objects.filter(issue_id=issue_id).order_by('-created_at').select_related().all()
    
    # TODO: THe status should be gotten from the session? so there is not query to DB every time!
    context['issue_is_pending'] = Issue.objects.get(id=issue_id).is_pending()                                                                                    
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
        amount_contributor_votes = Opinion_Vote.objects.filter(issue_id = issue_id).filter(contributor_id = request.user.id).count()
        if amount_contributor_votes < Opinion_Vote.MAX_VOTES_PER_CONTRIBUTOR:
            # Make new vote
            new_vote = Opinion_Vote.objects.create(
            issue_id = issue_id,
            opinion_id = opinion_id,
            contributor=request.user,
            vote = vote,     
            )
            # Check if this is a vote that allows the issue to go to PENDING state
            if is_issue_to_be_pending == True:
                return render(request, 'issue/pending_view.html') 
        else:
            
            return render(request, 'opinion/invalid_vote_view.html', {'message': _('You have voted more than 5 times! Please, remove one of your votes to vote again!')})
        
    
    # TODO: Double check if redirect is ok
    return redirect('read_opinion_view', issue_id = issue_id, opinion_id=opinion_id)

# Check if issue is ready to go be approved by Creators
# TODO: Validate votes against Article
def is_issue_to_be_pending(issue_id):
    issue_array = Issue.objects.filter(id=issue_id).aggregate(Count('issue_contributor'))
    if issue_array['issue_contributor__count'] < Issue.MIN_AMOUNT_CONTRIBUTORS:
        return False

    # Every opinion must have a positive vote.
    total_opinions_up_votes =  Opinion_Vote.objects.filter(issue_id = issue_id).filter(vote=1).values_list('opinion_id', flat=True).distinct().count()
    if total_opinions_up_votes < Opinion.TOTAL_OPINIONS_IN_ISSUE:
        return False
    
    # Total amount of possible votes must be 80%
    total_votes_in_opinions = Opinion_Vote.objects.filter(issue_id = issue_id).count()
    if total_votes_in_opinions < issue_array['issue_contributor__count'] * Opinion_Vote.MIN_PERCENTAGE_VOTES_IN_ISSUE * Opinion_Vote.MAX_VOTES_PER_CONTRIBUTOR:
        return False
    
    # Change status of issue
    issue = Issue.objects.get(id = issue_id)
    issue.status = Issue.PENDING
    issue.status_changed_at = datetime.now()
    issue.save(update_fields=['status', 'status_changed_at']) 
    return True
    
    
def create_opinion_view(request, issue_id):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = Opinion.objects.create(
            content=form.cleaned_data['content'],
            contributor=request.user,
            issue_id = issue_id,
            language = form.cleaned_data['language']
            )
            return redirect('opinions_view', issue_id = issue_id)  
    else:
        form = OpinionForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form
    context['contributor_id'] = request.user.id
    context['issue_id'] = issue_id
    return render(request, 'opinion/create_opinion_view.html', context)

def read_opinion_view(request, issue_id, opinion_id):
    context = {}
    context['contributor_id'] = request.user.id
    context['issue_id'] = issue_id
    # TODO: NOT DO IT HERE!
    user_voted =  Opinion_Vote.objects.filter(opinion_id = opinion_id).filter(contributor_id = request.user.id).filter(vote=1).values_list('vote', flat=True).distinct().count()
    if user_voted == 1:
        context['user_voted']= True
    else:
        context['user_voted'] = False
    context['total_votes'] = Opinion_Vote.objects.filter(opinion_id = opinion_id).count()
    
    # TODO: Order by most positive votes
    # TODO: Write this in a Manager?
    opinion = Opinion.objects.get(id=opinion_id)
                                                                                 
    context['opinion'] = opinion
    return render(request, 'opinion/read_opinion_view.html', context)
    