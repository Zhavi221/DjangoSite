from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from app import forms

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
             form.save()
             new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
             login(request, new_user)
             return HttpResponseRedirect('/')
        # log the user in
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
