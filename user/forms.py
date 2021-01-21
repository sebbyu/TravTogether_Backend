from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()
class CustomCreationForm(UserCreationForm):

  class Meta:
    model = User
    fields = ('email', 'nickname', 'profilePicture', 'gender', 'age', 
    'ethnicity', 'location', 'bio', 'password1', 'password2',)
    # fields = '__all__'

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

class MessageForm(forms.Form):
  sender = forms.CharField()
  receiver = forms.CharField()
  subject = forms.CharField()
  message = forms.CharField(widget=forms.Textarea)
