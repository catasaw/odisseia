from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.register, name='signup'),
    url(r'^signup/success/$', views.register_success, name='signup_success'),
]