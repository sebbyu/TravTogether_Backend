from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email', 'nickname', 'profile_picture', 'gender', 'age', 'race', 'password1', 'password2',)

class CustomChangeForm(UserChangeForm):
  class Meta:
    model = User
    # fields = ('email', 'nickname', 'profile_picture', 'gender', 'age', 'race', 'password')
    fields = '__all__'