from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import CustomCreationForm, UserRegistrationForm
from django.forms.models import model_to_dict
# from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly

User = get_user_model()
@api_view(['GET', 'POST'])
def userList(request):
	if request.method == "GET":
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		form = UserRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			nickname = form.cleaned_data.get('nickname')
			profilePicture = form.cleaned_data.get('profilePicture')
			gender = form.cleaned_data.get('gender')
			age = form.cleaned_data.get('age')
			ethnicity = form.cleaned_data.get('ethnicity')
			location = form.cleaned_data.get('location')
			password = form.cleaned_data.get('password')
			user = form.save(commit=False)
			user.set_password(password)
			serializer = UserSerializer(data=model_to_dict(user))
			if serializer.is_valid():
				serializer.save(profilePicture=request.data.get('profilePicture'))
				user = User.objects.get(email=email)
				user.set_password(password)
				user.save()
				return Response(data=serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


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
		print(email)
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=404)
	else:
		return HttpResponse(status=400)

