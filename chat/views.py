from django.shortcuts import render
from rest_framework import generics
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status


class ChatList(generics.ListCreateAPIView):
  queryset = Chat.objects.all()
  serializer_class = ChatSerializer

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Chat.objects.all()
  serializer_class = ChatSerializer


class MessageList(generics.ListCreateAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer