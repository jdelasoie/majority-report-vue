from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

import majority_report.views

# Routers provide an easy way of automatically determining the URL conf.
from surveys.urls import SurveyViewSet

router = routers.DefaultRouter()
router.register(r'users', majority_report.views.UserViewSet)
router.register(r'surveys', SurveyViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^$', majority_report.views.index),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
