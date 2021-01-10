from django import forms
from .models import Chat, Message
from django.contrib.auth import get_user_model
User = get_user_model()

class MessageForm(forms.Form):
  chatId = forms.IntegerField()
  userNickname = forms.CharField()
  newText = forms.CharField()

class ChatForm(forms.Form):
  title = forms.CharField()
  user = forms.CharField()

class AddChatUserForm(forms.Form):
  user = forms.CharField()