from django import forms
from .models import Chat, Message
from django.contrib.auth import get_user_model
User = get_user_model()

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = '__all__'

    def __init__(self, *args, **kwargs):
      super(Message, self).__init__(*args, **kwargs)

      self.fields['user'].queryset = User.objects.filter(User__in=chat)