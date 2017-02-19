from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^issue/(?P<issue_id>[0-9]+)/article/(?P<article_id>[0-9]+)/$', views.article_view, name='article_view'),
]