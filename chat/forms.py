from django import forms
from .models import Chat, Message
from django.contrib.auth import get_user_model
User = get_user_model()

class MessageForm(forms.Form):
  chatId = forms.IntegerField()
  userNickname = forms.CharField()
  newText = forms.CharField()
