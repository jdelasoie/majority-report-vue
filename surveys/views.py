# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the surveys index.")

def vote(request):
    return HttpResponse("Here we will have the ballot")
