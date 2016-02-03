from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^issues/pending/$', views.pending_issues_view, name='pending_issues_view'),
]