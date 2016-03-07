from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from magazine.models import Contributor, Language_Contributor, Language, Issue

# Create your views here.
@login_required
def profile(request):
    contributor = Contributor.objects.get(id=request.user.id)
    context = {}
    context['contributor'] = contributor
    context['first_language'] = Language.objects.filter(contributor = contributor, contributor_languages__type__exact=Language_Contributor.FIRST_LANGUAGE)
    context['second_language'] = Language.objects.filter(contributor = contributor, contributor_languages__type__exact=Language_Contributor.SECOND_LANGUAGE)
    context['published_issues'] = Issue.objects.order_by('-created_at').filter(status = Issue.PUBLISHED, issue_contributor__contributor_id=contributor.id)
    context['pending_issues'] = Issue.objects.order_by('-created_at').filter(status = Issue.PENDING, issue_contributor__contributor_id=contributor.id)
    context['in_progress_issues'] = Issue.objects.order_by('-created_at').filter(status = Issue.IN_PROGRESS, issue_contributor__contributor_id=contributor.id)
    return render(request, 'contributor_profile/profile_view.html', context)
    
