from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .models import Message
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate as myAuthenticate
from django.contrib.auth import login as myLogin
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CustomCreationForm, UserRegistrationForm, MessageForm
from django.forms.models import model_to_dict
# from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
from django.core.mail import BadHeaderError, send_mail
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
User = get_user_model()

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_field = 'slug'
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly,
	# IsOwnerOrReadOnly]


@csrf_exempt
def authentication(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = myAuthenticate(request, email=email, password=password)
		print(user)
		if user is not None:
			myLogin(request, user)
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=404)
	else:
		return HttpResponse(status=400)


@csrf_exempt
def contact(request):
	if request.method == "POST":
		name = request.POST.get('name', "")
		subject = request.POST.get('subject', "")
		message = request.POST.get('message', "")
		sendFrom = request.POST.get('sendFrom', "")
		tl = '\t'
		nl = '\n'
		message = f"From:{nl}{tl}{name}: {sendFrom}{nl}{nl}{message}"
		if subject and message and sendFrom:
			try:
				send_mail(subject, message, sendFrom, [os.getenv("EMAIL_HOST_USER")])
				return HttpResponse(status=200)
			except BadHeaderError:
				return HttpResponse("Invalid header found")
			return HttpResponseRedirect('/contact/thanks/')
		else:
			return HttpResponse("Make sure all fields are entered and valid")

@csrf_exempt
def sendMessage(request):
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			sender = form.cleaned_data['sender']
			receiver = form.cleaned_data['receiver']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			receiverUser = User.objects.get(nickname=receiver)
			new_message = Message(subject=subject, message=message, user=receiverUser,
			sender=sender)
			new_message.save()
			return HttpResponse(status=201) 
		print(form.errors)
		return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)