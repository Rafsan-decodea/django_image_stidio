from __future__ import unicode_literals ,print_function

from django.shortcuts import *

from .models import *
import smtplib
from django.http import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q


def index(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'src/blog/blog_page.html' , context)

def login_panal(request):
    return render(request,'login.html')



##def register(request):
##    form = UserCreationForm()
##    if request.method == 'POST':
##        form = UserCreationForm(request.POST)
##        if form.is_valid():
##            form.save()
##    context = {'form':form}


def login(request):
   context ={}
   if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'login.html',{'error':'User name or password not matching'})
   else:
    return  render(request, 'login.html',context)
def user_logout(request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))











# Create your views here.
