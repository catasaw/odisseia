from django.shortcuts import render
from magazine.models import Issue
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.

@login_required
def pending_issues_view(request):
    pending_issues = Issue.objects.order_by('-created_at').filter(status = Issue.PENDING)
    paginator = Paginator(pending_issues, 12)
    page = request.GET.get('page')
    return render(request, 'issue/pending_issues_view.html', {'issues': pending_issues})

@login_required
def update_status_issue_view(request, issue_id, status):
    try: 
        issue = Issue.objects.get(id = issue_id)
    except Issue.DoesNotExist:
        return render(request, 'issue/issue_does_not_exist_view.html')
    
    if status == 'approve':
        issue.status = Issue.APPROVED
    else:
        issue.status = Issue.REJECTED
    
    issue.status_changed_at = datetime.now()
    issue.save(update_fields=['status', 'status_changed_at'])
    return render(request, 'issue/successful_change_status.html')