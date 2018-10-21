from django.shortcuts import render, redirect
from rest_framework.views import APIView
from users.forms import SignUpForm
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import list_route
from users.permissions import IsLoggedInUser
from users.models import user
from users.serializers import UserSerializer

# import pdb

# Create your views here.
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/admin/')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


class ProfileAPI(viewsets.ViewSet):
    @list_route(
        methods=['get', 'post'],
        url_path='profile',
        url_name='profile',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        query_set = user.objects.filter(email=request.user).values('email', 'first_name', 'last_name')
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)