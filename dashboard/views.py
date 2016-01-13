from django.shortcuts import render
from magazine.models import Issue
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    latest_issues = Issue.objects.order_by('created_at').filter(published_at__isnull=True)[:6]
    return render(request, 'dashboard/issues_dashboard.html', {'issues': latest_issues,})

@login_required
def new_issue_view(request):
    return render(request, 'dashboard/new_issue_view.html')