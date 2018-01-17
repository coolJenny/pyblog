from django.conf.urls import *
from . import views

urlpatterns = [
 url(r'^hello/$', views.hello),
 url(r'^$', views.post_list, name='post_list'),
]