# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import NewUserForm
# from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
	
# Create your views here.

def home(request):
	return render(request, 'home.html',{'name':'Lakshmi'})

def add(request):

	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])

	res  = val1 + val2
	return render(request, 'result.html',{'result':res})

def register(request):
		if request.method == "POST":
			form = UserCreationForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				login(request, user)
				return render(request = request,
							  template_name = "home.html",
							  )

			else:
				for msg in form.error_messages:
					print(form.error_messages[msg])

				return render(request = request,
							  template_name = "register.html",
							  context={"form":form})

		form = UserCreationForm
		return render(request = request,
					  template_name = "register.html",
					  context={"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username") 
			password = form.cleaned_data.get("password")
			user = authenticate(username = username, password = password)

			if user is not None:
				login(request, user)
				messages.success(request, f"You are now logged in with {username}")
				return  render(request = request,
					   		   template_name = "home.html"
					   		   )
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "login.html",
				  {"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logout Successfully")
	return render(request,
				  "home.html")