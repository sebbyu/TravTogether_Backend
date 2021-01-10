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
from .forms import MessageForm, ChatForm, AddChatUserForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
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

def chat_room(request, chat_id):
  try:
    chat = get_object_or_404(Chat, pk=chat_id)
  except:
    return HttpResponse(status=404)
  return HttpResponse(chat, status=200)

@csrf_exempt
@api_view(['GET', 'POST'])
def chatList(request):
  if request.method == "GET":
    chats = Chat.objects.all()
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == "POST":
    form = ChatForm(request.POST)
    if form.is_valid():
      title = form.cleaned_data['title']
      userNickname = form.cleaned_data['user']
      user = User.objects.get(nickname=userNickname)
      print(user)
      chat = Chat(title=title)
      print(chat)
      chat.save()
      chat.users.add(user)
      return HttpResponse(chat, status=201)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def chatDetail(request, chat_id):
  chat = Chat.objects.get(id=chat_id)
  if request.method == "GET":
    serializer = ChatSerializer(chat)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == "PUT":
    form = AddChatUserForm(request.POST)
    if form.is_valid():
      userNickname = form.cleaned_data['user']
      user = User.objects.get(nickname=userNickname)
      chat.users.add(user)
      return HttpResponse(chat, status=200)
    print(form.errors)
    return HttpResponse(chat, status=201)
  elif request.method == "DELETE":
    chat.delete()
    return HttpResponse(status=204)