from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^newissue/$', views.new_issue_view, name='new_issue_view'),
    url(r'^issue/join/(?P<issue_id>[0-9]+)/$', views.join_issue_view, name='join_issue_view'),
    url(r'^issue/success/(?P<issue_id>[0-9]+)/$', views.join_issue_successful_view, name='join_issue_successful_view'),
]