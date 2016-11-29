from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from . import views


urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', views.homepage, name='odisseia'),
    url(r'^imprint/$', views.imprint, name='imprint'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
);