from django.shortcuts import render
from magazine.models import Issue
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

@login_required
def pending_issues_view(request):
    pending_issues = Issue.objects.order_by('-created_at').filter(status = Issue.PENDING)
    paginator = Paginator(pending_issues, 12)
    page = request.GET.get('page')
    return render(request, 'issue/pending_issues_view.html', {'issues': pending_issues})
