from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()
class CustomCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email', 'nickname', 'profilePicture', 'gender', 'age', 'ethnicity', 'password1', 'password2',)

class CustomChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = '__all__'

class UserRegistrationForm(forms.ModelForm):
  email = forms.EmailField(required=True)
  nickname = forms.CharField(required=False)
  profilePicture = forms.ImageField(required=False)
  gender = forms.CharField(required=False)
  age = forms.CharField(required=False)
  ethnicity = forms.CharField(required=False)
  location = forms.CharField(required=True)
  password = forms.CharField(widget=forms.PasswordInput, required=True)
  class Meta:
    model = User
    fields = ['email', 'nickname', 'profilePicture', 'gender', 'age', 'ethnicity', 'password',]
    # fields = ['email', 'nickname', 'gender', 'age', 'ethnicity', 'location', 'password',]