import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.user = self.scope['user']
    # print(self.scope)
    self.id = self.scope['url_route']['kwargs']['chat_id']
    self.room_group_name = 'chat_%s' % self.id
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
    userNickname, newText = text_data_json['userNickname'], \
    text_data_json['newText']
    now = timezone.now()
    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'chat_message',
        'message': newText,
        'user': self.user.username,
        'userNickname': userNickname,
        'created': now.isoformat(),
      }
    )
    # self.send(text_data=json.dumps({'userNickname': userNickname,
    # 'newText': newText}))
  def chat_message(self, event):
    self.send(text_data=json.dumps(event))