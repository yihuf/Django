# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context


# Create your views here.
def index(request):
    mystr = 'hello ddddd'
    t = loader.get_template('polls/index.html')
    c = {'mystr': mystr}
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    return HttpResponse("hello world,you are at the detail polls%s" % poll_id)

def results(request, poll_id):
    return HttpResponse("hello world,you are at the poll results%s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("hello world,you are at the poll vote%s" % poll_id)

