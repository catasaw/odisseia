from django.conf.urls import url

from . import views
from magazine.homepageview import HomepageView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='odisseia'),
]