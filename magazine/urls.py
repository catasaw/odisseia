from django.conf.urls import url

from . import views
from magazine.homepageview import HomepageView
from magazine.signupview import SignupView


urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='odisseia'),
    url(r'^signup/', SignupView.as_view(), name='signup'),
    #url(r'^createuser/', UserView.as_view(), name='user'),
]