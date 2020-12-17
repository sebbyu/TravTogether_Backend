from django import forms
from .models import Question


class QuestionForm(forms.Form):
  question = forms.CharField()
  
  class Meta:
    model = Question
    fields = ('question',)
