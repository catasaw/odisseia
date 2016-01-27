from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^issue/(?P<issue_id>[0-9]+)/opinions/$', views.opinions_view, name='opinions_view'),
    url(r'^issue/(?P<issue_id>[0-9]+)/opinion/(?P<opinion_id>[0-9]+)/vote/(?P<vote_type>(up|down)+)/$', views.vote_view, name='vote_view'),
]