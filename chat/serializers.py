from rest_framework import serializers
from .models import Chat, Message
from user.serializers import UserSerializer

class ChatSerializer(serializers.ModelSerializer):

  users = serializers.StringRelatedField(many=True)
  messages = serializers.StringRelatedField(many=True)
  class Meta:
    model = Chat
    fields = ['title', 'created', 'users', 'messages',]

class MessageSerializer(serializers.ModelSerializer):

  User = serializers.StringRelatedField()
  class Meta:
    model = Message
    fields = ['text', 'created', 'user',]