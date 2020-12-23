from django.urls import path
from . import views as base_views
from qanda import views as qanda_views
from user import views as user_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  path('', base_views.api_root),
  # path('users/', user_views.userList, name='user-list'),
  path('users/', user_views.UserList.as_view(), name='user-list'),
  path('users/<slug:slug>/', user_views.UserDetail.as_view(), name='user-detail'),
  path('questions/', qanda_views.QuestionList.as_view(), name='question-list'),
  path('questions/<slug:slug>/', qanda_views.QuestionDetail.as_view(), name='question-detail'),
  path('answers/', qanda_views.AnswerList.as_view(), name='answer-list'),
  path('answers/<int:pk>/', qanda_views.AnswerDetail.as_view(), name='answer-detail'),

  path('authentication/', user_views.authentication)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)