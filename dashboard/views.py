from django.shortcuts import render, render_to_response
from magazine.models import Issue, Issue_Contributor
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from dashboard.issueform import IssueForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf

@login_required
def dashboard(request):
    latest_issues = Issue.objects.order_by('created_at').filter(published_at__isnull=True)[:6]
    return render(request, 'dashboard/issues_dashboard.html', {'issues': latest_issues,})

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