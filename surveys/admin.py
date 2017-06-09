# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from surveys.models import Survey, Vote, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class SurveyAdmin(admin.ModelAdmin):
    model = Survey

    inlines = [
        ChoiceInline,
    ]


admin.site.register(Survey, SurveyAdmin)
