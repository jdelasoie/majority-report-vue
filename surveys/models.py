# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=50)
    comment = models.TextField(max_length=512,
                               help_text="Rédigez un commentaire indiquant "
                                         "aux destinataires pourquoi vous"
                                         " les sollicitez, et à quoi "
                                         "serviront les résultats.")
    date_limit = models.DateTimeField('date published')


class Choice(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)


class Vote(models.Model):
    REJECT = "REJECT"
    INSUFFISANT = "INSUFFISANT"
    PASSABLE = "PASSABLE"
    ASSEZ_BIEN = "ASSEZ_BIEN"
    BIEN = "BIEN"
    TRES_BIEN = "TRES_BIEN"
    EXCELLENT = "EXCELLENT"

    JUDGMENT_CHOICES = (
        (REJECT, "A rejeter"),
        (INSUFFISANT, "Insuffisant-e"),
        (PASSABLE, "Passable"),
        (ASSEZ_BIEN, "Assez bien"),
        (BIEN, "Bien"),
        (TRES_BIEN, "Très bien"),
        (EXCELLENT, "Excellent"),
    )

    voter = models.ForeignKey(User)
    judgment = models.CharField(max_length=55,
                                choices=JUDGMENT_CHOICES)
