from rest_framework import serializers
from surveys.models import Survey, Choice


class SurveyVotesListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Choice: %s, votes count: %s' % (value.choice_text, value.votes.count())


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    choices = SurveyVotesListingField(many=True, read_only=True)


    class Meta:
        model = Survey
        fields = '__all__'


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
