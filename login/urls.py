from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/signup/$', views.register, name='signup'),
    url(r'^accounts/login/$', views.login_view, name='login_view'),
    url(r'^accounts/logout/$', views.logout_view, name='logout_view'),
    url(r'^signup/success/$', views.register_success, name='signup_success'),
]