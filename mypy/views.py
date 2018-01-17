# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
 text = "<h1>welcome to my app</h1>"
 return HttpResponse(text)

# def hello(request):
#  return render(request, "mypy/templates/hello.html", {})

def post_list(request):
	return render(request, 'blog/post_list.html')