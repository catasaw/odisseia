from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^newissue/$', views.new_issue_view, name='new_issue_view'),
]