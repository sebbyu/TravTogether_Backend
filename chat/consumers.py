import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
from .models import Chat, Message
from .serializers import MessageSerializer
from user.models import User
from django.forms.models import model_to_dict



class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.user = self.scope['user']
    self.chat_id = self.scope['url_route']['kwargs']['chat_id']
    self.room_group_name = 'chat_%s' % self.chat_id
    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )
    self.accept()

  def disconnect(self, close_code):
    async_to_sync(self.channel_layer.group_discard)(
      self.room_group_name,
      self.channel_name
    )
  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    userNickname, newText = text_data_json['userNickname'], text_data_json['newText']
    now = timezone.now()
    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'chat_message',
        'newText': newText,
        'userNickname': userNickname,
        'created': now.isoformat(),
      }
    )
    self.addToServer(newText, userNickname)

  def chat_message(self, event):
    self.send(text_data=json.dumps(event))

  def addToServer(self, newText, userNickname):
    chat = Chat.objects.get(id=self.chat_id)
    user = User.objects.get(nickname=userNickname)
    message = Message(text=newText,chat=chat,user=user)
    message.save()