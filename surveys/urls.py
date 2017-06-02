from rest_framework import viewsets

from surveys.models import Survey

# ViewSets define the view behavior.
from surveys.serializers import SurveySerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
