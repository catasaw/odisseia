from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^issue/(?P<issue_id>[0-9]+)/articles/$', views.articles_view, name='articles_view'),
]