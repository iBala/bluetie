from django.shortcuts import render, redirect
from rest_framework.views import APIView
from users.forms import SignUpForm
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.reverse import reverse

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

