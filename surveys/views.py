# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.core import serializers

from surveys.models import Survey


def index(request):
    serialized_queryset = serializers.serialize('json', Survey.objects.all())
    return JsonResponse(serialized_queryset, safe=False)


def vote(request):
    return HttpResponse("Here we will have the ballot")
