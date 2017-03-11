from django.shortcuts import render
from django.http import HttpResponse
from .models import Introduction,Article,Issue
from datetime import datetime, timedelta
from django.utils.timezone import utc

def homepage(request):
    # return render(request, 'magazine/welcome_homepage_view.html')
    # TODO: If first time to query issue, then cache it?
    # Check latest PUBLISHED issue
    try:
        last_published_issue = Issue.objects.filter(status = Issue.PUBLISHED).latest('status_changed_at')
        return render(request, 'magazine/welcome_homepage_view.html', {'issue': last_published_issue, 'none_articles': range(Article.TOTAL_ARTICLES_IN_ISSUE - last_published_issue.article_set.count())}) 
    except Issue.DoesNotExist:
        earliest_approved_issue= publish_earliest_approved_issue()
        if earliest_approved_issue is None:
            # Render expectation page
            return render(request, 'magazine/welcome_homepage_view.html')
        
        return render(request, 'magazine/welcome_homepage_view.html', {'issue': earliest_approved_issue, 'none_articles': range(Article.TOTAL_ARTICLES_IN_ISSUE - earliest_approved_issue.article_set.count())})
    
    
    # if Issue exist, check that is longer than 2 weeks
    earliest_approved_issue = publish_earliest_approved_issue()
    
    if (datetime.now().replace(tzinfo=utc) - last_published_issue.status_changed_at.replace(tzinfo=utc)).days   > 14:
    #if datetime.now() -  timedelta(weeks=2) < last_published_issue.status_changed_at  :
        if earliest_approved_issue is None:
            # Render homepage with previous issue
            return render(request, 'magazine/welcome_homepage_view.html', {'issue': last_published_issue, 'none_articles': range(Article.TOTAL_ARTICLES_IN_ISSUE - last_published_issue.article_set.count())})
        
    
    # Render homepage with earliest approved issue
    return render(request, 'magazine/welcome_homepage_view.html', {'issue': last_published_issue, 'none_articles': range(Article.TOTAL_ARTICLES_IN_ISSUE - last_published_issue.article_set.count())})

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

def imprint(request):
    return render(request, 'magazine/imprint.html')

def credits(request):
    return render(request, 'magazine/credits.html')