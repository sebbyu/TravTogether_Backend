from django.contrib import admin
from .models import Question, Answer

  

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
  list_display = ('id', 'question',)
  prepopulated_fields = {"slug": ("question",)}

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
  list_display = ('id', 'question', 'answer',)