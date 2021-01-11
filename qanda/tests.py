from django.test import TestCase
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
# Create your tests here.

class QandATestCase(TestCase):
  def setUp(self):
    Question.objects.create(question="What is question1?")
    Question.objects.create(question="What is question2?")
    Question.objects.create(question="What is question3?")
    Question.objects.create(question="What is question4?")
    Answer.objects.create(answer="This is answer1!")
    Answer.objects.create(answer="This is answer2!")
    Answer.objects.create(answer="This is answer3!")
    Answer.objects.create(answer="This is answer4!")

    self.q1 = Question.objects.get(question="What is question1?")
    self.q2 = Question.objects.get(question="What is question2?")
    self.q3 = Question.objects.get(question="What is question3?")
    self.q4 = Question.objects.get(question="What is question4?")

    self.a1 = Answer.objects.get(answer="This is answer1!")
    self.a2 = Answer.objects.get(answer="This is answer2!")
    self.a3 = Answer.objects.get(answer="This is answer3!")
    self.a4 = Answer.objects.get(answer="This is answer4!")

    self.qSer1 = QuestionSerializer(instance=self.q1)
    self.qSer2 = QuestionSerializer(instance=self.q2)
    self.aSer1 = AnswerSerializer(instance=self.a1)
    self.aSer2 = AnswerSerializer(instance=self.a2)
  
  def test_answer(self):
    self.a1.question = self.q1
    self.a2.question = self.q2
    self.a3.question = self.q3
    self.a4.question = self.q4

    self.assertEqual(self.a1.question, self.q1)
    self.assertEqual(self.a2.question, self.q2)
    self.assertEqual(self.a3.question, self.q3)
    self.assertEqual(self.a4.question, self.q4)
