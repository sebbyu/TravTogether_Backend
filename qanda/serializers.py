from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  answers = serializers.StringRelatedField(
    many=True,
  )
  class Meta:
    model = Question
    fields = ['url', 'question', 'answers',]
    extra_kwargs = {'url': {'lookup_field': 'slug'}}


class AnswerSerializer(serializers.ModelSerializer):
  question = serializers.StringRelatedField()
  class Meta:
    model = Answer
    fields = '__all__'