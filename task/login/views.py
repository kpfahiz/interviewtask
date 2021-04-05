from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import  CreateUserForm


def signUp(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('core:login')
        context = {'form':form}
        return render(request, 'signup.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('core:home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				return redirect('core:home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def home(request):
    users = User.objects.all()
    context={
        'users':users
    }
    return render(request, 'home.html', context)
