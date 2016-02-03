from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^issues/pending/$', views.pending_issues_view, name='pending_issues_view'),
    url(r'^issue/(?P<issue_id>[0-9]+)/(?P<status>(approve|reject)+)/$', views.update_status_issue_view, name='update_status_issue_view'),
]