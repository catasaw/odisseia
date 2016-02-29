from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views


urlpatterns = patterns('', 
    url(r'^$', views.homepage, name='odisseia'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
);