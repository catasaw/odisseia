from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^issue/(?P<issue_id>[0-9]+)/introduction/(?P<introduction_id>[0-9]+)$', views.introduction_view, name='introduction_view'),
]