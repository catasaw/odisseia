from django.shortcuts import render
from magazine.models import Issue

def dashboard(request):
    latest_issues = Issue.objects.order_by('created_at').filter(published_at__isnull=True)[:6]
    return render(request, 'dashboard/issues_dashboard.html', {'issues': latest_issues,})