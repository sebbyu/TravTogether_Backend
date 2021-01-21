from django.urls import path
from . import views as base_views
from qanda import views as qanda_views
from user import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from chat import views as chat_views


urlpatterns = [
  path('', base_views.api_root),
  path('users/', user_views.UserList.as_view(), name='user-list'),
  path('users/<slug:slug>/', user_views.UserDetail.as_view(), name='user-detail'),
  path('questions/', qanda_views.QuestionList.as_view(), name='question-list'),
  path('questions/<slug:slug>/', qanda_views.QuestionDetail.as_view(), name='question-detail'),
  path('answers/', qanda_views.AnswerList.as_view(), name='answer-list'),
  path('answers/<int:pk>/', qanda_views.AnswerDetail.as_view(), name='answer-detail'),

  path('authentication/', user_views.authentication),
  path('contact/', user_views.contact),
  path('sendMessage/', user_views.sendMessage),
  # path('chats/', chat_views.ChatList.as_view(), name="chat-list"),
  # path("chats/<int:pk>/", chat_views.ChatDetail.as_view(), name="chat-detail"),
  path('chats/', chat_views.chatList, name="chat-list"),
  path('chats/<int:chat_id>/', chat_views.chatDetail, name="chat-detail"),
  # path("messages2/", chat_views.MessageList.as_view(), name="message-list"),
  path("messages/", chat_views.messageList, name="message-list"),
  path("messages/<int:pk>/", chat_views.MessageDetail.as_view(), name="message-detail"),
  path("chatroom/<int:chat_id>/", chat_views.chat_room, name="chat_room"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
