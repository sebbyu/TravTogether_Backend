import json
from channels.generic.websocket import WebsocketConsumer
class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.accept()
  def disconnect(self, close_code):
    pass
  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    userNickname, newText = text_data_json['userNickname'], \
    text_data_json['newText']
    self.send(text_data=json.dumps({'userNickname': userNickname,
    'newText': newText}))