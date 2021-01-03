from rest_framework import serializers
from .models import Chat, Message
from user.serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class ChatSerializer2(serializers.ModelSerializer):

  class Meta:
    model = Chat
    fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):

  user = UserSerializer
  chat = ChatSerializer2
  class Meta:
    model = Message
    fields = ['id', 'text', 'created', 'chat', 'user']

  def to_representation(self, instance):
    response = super().to_representation(instance)
    response['chat'] = self.represent_chat(
      ChatSerializer2(instance.chat).data)
    response['user'] = self.represent_user(
      UserSerializer(instance.user).data)
    return response
  def represent_chat(self, chat_data):
    temp = dict()
    temp['id'] = chat_data['id']
    temp['title'] = chat_data['title']
    temp['created'] = chat_data['created']
    return temp
  def represent_user(self, user_data):
    return user_data['nickname']


class ChatSerializer(serializers.ModelSerializer):

  users = serializers.StringRelatedField(many=True)
  messages = MessageSerializer(many=True)
  class Meta:
    model = Chat
    fields = ['id', 'title', 'created', 'users', "messages", ]
  
  def to_representation(self, instance):
    response = super().to_representation(instance)
    messages = []
    for value in response['messages']:
      temp = dict()
      temp['user'] = value['user']
      temp['text'] = value['text']
      temp['created'] = value['created']
      messages.append(temp)
    result = {'id': response['id'],
              'title': response['title'],
              'created': response['created'],
              'users': response['users'],
              'messages': messages}
    return result
