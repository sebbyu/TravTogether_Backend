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

