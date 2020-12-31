from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CustomCreationForm, UserRegistrationForm
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
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=404)
	else:
		return HttpResponse(status=400)


@csrf_exempt
def sendMessage(request):
	if request.method == "POST":
		subject = request.POST.get('subject', "")
		message = request.POST.get('message', "")
		fromEmail = request.POST.get('fromEmail', "")
		nl = '\n'
		message = f"From:{nl}{fromEmail}{nl}{message}"
		if subject and message and fromEmail:
			try:
				send_mail(subject, message, fromEmail, ['ystephen0522@gmail.com'])
				return HttpResponse(status=200)
			except BadHeaderError:
				return HttpResponse("Invalid header found")
			return HttpResponseRedirect('/contact/thanks/')
		else:
			return HttpResponse("Make sure all fields are entered and valid")

@csrf_exempt
def sendEmail(request):
	if request.method == "POST":
		sendFrom = request.POST.get("sendFrom", "")
		sendTo = request.POST.get("sendTo", "")
		subject = request.POST.get("subject", "")
		message = request.POST.get("message", "")

		msg = EmailMessage()
		msg.set_content(message)
		msg['Subject'] = subject
		msg['From'] = sendFrom
		msg['To'] = sendTo

		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login(os.getenv("EMAIL_HOST_USER"), os.getenv("EMAIL_HOST_PASSWORD"))
		server.send_message()
		server.quit()
		return HttpResponse(status=200)
