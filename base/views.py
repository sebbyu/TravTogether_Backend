from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'Users': reverse('user-list', request=request, format=format),
    'Questions': reverse('question-list', request=request, format=format),
    'Answers': reverse('answer-list', request=request, format=format),
    "Chats": reverse('chat-list', request=request, format=format),
    "Messages": reverse('message-list', request=request, format=format),
  })
    
