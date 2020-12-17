from rest_framework import generics
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionList(generics.ListCreateAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  lookup_field='slug'

class AnswerList(generics.ListCreateAPIView):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer