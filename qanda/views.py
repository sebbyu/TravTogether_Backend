from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from .forms import QuestionForm
from django.forms.models import model_to_dict


class QuestionList(generics.ListCreateAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

# @api_view(['GET', 'POST'])
# def questionList(request):
#   if request.method == 'GET':
#     questions = Question.objects.all()
#     serializer = QuestionSerializer(questions, many=True)
#     return Response(serializer.data)
#   elif request.method == 'POST':
#     form = QuestionForm(request.POST)
#     if form.is_valid():
#       question = form.cleaned_data.get('question')
#       q_object = form.save(commit=False)
#       serializer = QuestionSerializer(data=model_to_dict(q_object))
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

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