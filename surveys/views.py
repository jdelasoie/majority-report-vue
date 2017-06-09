# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.core import serializers

from rest_framework import viewsets
from rest_framework import generics, mixins, views
from surveys.models import Survey, Choice, Vote

# ViewSets define the view behavior.
from surveys.serializers import SurveySerializer, ChoiceSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = Choice

    # TODO: draw a custom choice form


def index(request):
    serialized_queryset = serializers.serialize('json', Survey.objects.all())
    return JsonResponse(serialized_queryset, safe=False)


def vote(request):
    return HttpResponse("Here we will have the ballot")