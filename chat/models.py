from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
User = get_user_model()


class Chat(models.Model):
  title = models.CharField(_("title"), max_length=50, blank=True)
  users = models.ManyToManyField(User, related_name="chats")
  created = models.DateTimeField(_("created"), auto_now_add=True)

  class Meta:
    ordering = ['-created',]
  
  def __str__(self):
    return f"{self.title} - {self.created.now()}"

class Message(models.Model):
  text = models.CharField(_("text"), max_length=250)
  created = models.DateTimeField(_("created"), auto_now_add=True)
  chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  class Meta:
    ordering = ['-created',]
  
  def __str__(self):
    return f"{self.user}: {self.text} - {self.created.now()}"