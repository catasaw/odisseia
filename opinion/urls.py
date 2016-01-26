from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^issue/(?P<issue_id>[0-9]+)/opinions/$', views.opinions_view, name='opinions_view'),
]