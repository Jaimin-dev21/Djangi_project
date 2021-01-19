from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):

	dests = Destination.objects.all()
	return render(request,"index.html" , {'dests' : dests})

def destination(request):
	if request.user.is_authenticated:
		return render(request,'destination.html')
	else:
		return render(request,'login.html')

