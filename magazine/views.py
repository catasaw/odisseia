from django.shortcuts import render
from django.http import HttpResponse
from .models import Opinion,Article,Issue
from datetime import datetime

def homepage(request):
    # TODO: If first time to query issue, then cache it?
    # Check latest PUBLISHED issue
    try:
        last_published_issue = Issue.objects.filter(status = Issue.PUBLISHED).latest('status_changed_at')
    except Issue.DoesNotExist:
        earliest_approved_issue= publish_earliest_approved_issue()
        if earliest_approved_issue is None:
            # Render expectation page
            return render(request, 'magazine/welcome_homepage_view.html')
        
        return render(request, 'magazine/homepage.html', {'issue': earliest_approved_issue})

    # if Issue exist, check that is longer than 2 weeks
    if last_published_issue.status_changed_at > '2 weeks ':
        earliest_approved_issue= publish_earliest_approved_issue()
        if earliest_approved_issue is None:
            # Render homepage with previous issue
            return render(request, 'magazine/homepage.html', {'issue': last_published_issue})
        
        # Render homepage with earliest approved issue
        return render(request, 'magazine/homepage.html', {'issue': earliest_approved_issue})

# view method
def publish_earliest_approved_issue():
    try:
            last_issue = Issue.objects.filter(status = Issue.APPROVED).earliest('status_changed_at')
    except Issue.DoesNotExist:
            return None
    # Change status of issue to publish and display it
    last_issue.status = Issue.PUBLISHED
    last_issue.status_changed_at = datetime.now()
    last_issue.save(update_fields=['status', 'status_changed_at'])
    return last_issue