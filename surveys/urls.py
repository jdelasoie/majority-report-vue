from django.conf.urls import url

import surveys.views

urlpatterns = [
    url(r'^$', surveys.views.index),
]
