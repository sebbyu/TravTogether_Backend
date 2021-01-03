from django.shortcuts import render
from rest_framework import generics
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .forms import MessageForm
from django.contrib.auth import get_user_model
User = get_user_model()


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

@csrf_exempt
@api_view(['GET', 'POST'])
def messageList(request):
  if request.method == "GET":
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == "POST":
    form = MessageForm(request.POST)
    if form.is_valid():
      chatId = form.cleaned_data['chatId']
      newText = form.cleaned_data['newText']
      userNickname = form.cleaned_data['userNickname']
      chat = Chat.objects.get(id=chatId)
      user = User.objects.get(nickname=userNickname)
      message = Message(text=newText,chat=chat,user=user)
      serializer = MessageSerializer(data=model_to_dict(message))
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      print(serializer.error_messages)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    print(form.errors)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)