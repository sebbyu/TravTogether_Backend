from django.contrib import admin
from .models import Question, Answer

  

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
  list_display = ('id', 'question',)

  fieldsets = (
    (None, {'fields': ('question',)}),
  )

  add_fieldsets = (
    (None, {'classes': ('wide',),
    'fields': ('question',)}),
  )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
  list_display = ('id', 'question', 'answer',)