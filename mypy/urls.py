from django.conf.urls import *
from . import views

urlpatterns = [
 url(r'^hello/$', views.hello),
]