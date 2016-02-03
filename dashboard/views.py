from django.shortcuts import render, render_to_response, redirect
from magazine.models import Issue, Issue_Contributor
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from dashboard.issueform import IssueForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@login_required
def dashboard(request):
    latest_issues = Issue.objects.exclude(issue_contributors__id = request.user.id).order_by('-created_at').filter(status = Issue.IN_PROGRESS)
    paginator = Paginator(latest_issues, 12)
    page = request.GET.get('page')
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, return first page
        issues = paginator.page(1)
    except EmptyPage:
        # If page is out of range, return last page of results
        issues = paginator.page(paginator.num_pages)

    return render(request, 'dashboard/issues_dashboard.html', {'issues': issues, 'issues_current_user': request.user.issue_set.all,})

@login_required
@csrf_protect
def new_issue_view(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            new_issue = Issue(
            title=form.cleaned_data['title']
             )
            new_issue.save()
            new_issue_contributor = Issue_Contributor(
            issue=new_issue,
            contributor=request.user
            )
            new_issue_contributor.save()
            return HttpResponseRedirect('/dashboard/')     
    else:
        form = IssueForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form
    return render(request, 'dashboard/new_issue_view.html', context)

@login_required
def join_issue_view(request, issue_id):
    try:
        issue_contributor=Issue_Contributor.objects.get(issue_id=issue_id, contributor_id= request.user.id)
    except Issue_Contributor.DoesNotExist:
        new_issue_contributor = Issue_Contributor(
            issue_id=issue_id,
            contributor=request.user
            )
        new_issue_contributor.save()
        request.session['issue_id'] = issue_id
        return redirect('join_issue_successful_view', issue_id = issue_id)
    
    return redirect('issue_view', issue_id = issue_id)

@login_required
def join_issue_successful_view(request, issue_id):
    context = {}
    context['issue_id'] = issue_id
    return render(request, 'dashboard/join_issue_successful.html', context)
    
    
    