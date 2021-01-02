from django.contrib import admin
from .models import Chat, Message
from .forms import MessageForm


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
  list_display = ('title', 'id', 'created',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ('text', 'created', "chat_id", "user_id",)